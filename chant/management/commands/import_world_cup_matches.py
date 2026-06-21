import re
import urllib.error
import urllib.request
from datetime import date, datetime, time, timedelta, timezone
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from club.models import Club
from chant.models import Match

DEFAULT_TOURNAMENT = "2026"
LONDON = timezone(timedelta(hours=0))  # stored as UTC after conversion

MONTHS = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12,
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
}

DATE_RE = re.compile(
    r"^(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun)\s+"
    r"(Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|"
    r"Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+"
    r"(\d{1,2})$"
)
MATCH_LINE_RE = re.compile(
    r"^\s*(?:\(\d+\)\s+)?"
    r"(\d{1,2}):(\d{2})\s+UTC([+-])(\d+)\s+"
    r"(.+?)\s+@\s+.+$"
)
SCORE_SPLIT_RE = re.compile(r"^(.+?)\s+\d+-\d+(?:\s+\(\d+-\d+\))?\s+(.+)$")
PLACEHOLDER_TEAM_RE = re.compile(
    r"^(\d+[A-Z](?:/\d+[A-Z])*(?:/[A-Z])?|[WL]\d+|3[A-Z](/[A-Z])+(?:/\d+[A-Z])?)$"
)

# OpenFootball names -> club names in this project.
TEAM_ALIASES = {
    "USA": "United States",
    "Bosnia & Herzegovina": "Bosnia and Herzegovina",
    "Curaçao": "Curacao",
}


def tournament_paths(tournament):
    base = Path(settings.BASE_DIR) / "data" / "match"
    return (
        base / f"world_cup_{tournament}.txt",
        base / f"world_cup_{tournament}_finals.txt",
    )


def tournament_download_urls(tournament):
    folder = f"{tournament}--usa"
    base = f"https://raw.githubusercontent.com/openfootball/worldcup/master/{folder}"
    return (
        f"{base}/cup.txt",
        f"{base}/cup_finals.txt",
    )


class Command(BaseCommand):
    help = "Import World Cup fixtures from OpenFootball Football.TXT format."

    def add_arguments(self, parser):
        parser.add_argument(
            "--tournament",
            type=str,
            default=DEFAULT_TOURNAMENT,
            help="Tournament year tag (default: 2026).",
        )
        parser.add_argument(
            "--group-stage",
            type=str,
            help="Path to group-stage fixture file.",
        )
        parser.add_argument(
            "--knockout",
            type=str,
            help="Path to knockout fixture file.",
        )
        parser.add_argument(
            "--download",
            action="store_true",
            help="Download fixture files from OpenFootball before importing.",
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Parse and report without writing to the database.",
        )

    def handle(self, *args, **options):
        tournament = options["tournament"]
        default_group, default_knockout = tournament_paths(tournament)
        group_path = Path(options["group_stage"] or default_group).expanduser().resolve()
        knockout_path = Path(options["knockout"] or default_knockout).expanduser().resolve()

        if options["download"]:
            self._download(group_path, knockout_path, tournament)

        sources = [path for path in (group_path, knockout_path) if path.is_file()]
        if not sources:
            raise CommandError(
                "No fixture files found. Run with --download or add files under data/match/."
            )

        year = int(tournament)
        fixtures = []
        for source in sources:
            fixtures.extend(parse_world_cup_fixtures(source.read_text(encoding="utf-8"), year=year))

        if not fixtures:
            raise CommandError("No fixtures parsed.")

        club_map = self._build_club_map()
        created = skipped = placeholders = missing = 0
        missing_teams = set()
        dry_run = options["dry_run"]

        with transaction.atomic():
            for fixture in fixtures:
                home_name = fixture["home"]
                away_name = fixture["away"]
                if PLACEHOLDER_TEAM_RE.match(home_name) or PLACEHOLDER_TEAM_RE.match(away_name):
                    placeholders += 1
                    continue

                home = club_map.get(home_name)
                away = club_map.get(away_name)
                if home is None:
                    missing_teams.add(home_name)
                    missing += 1
                    continue
                if away is None:
                    missing_teams.add(away_name)
                    missing += 1
                    continue

                if dry_run:
                    created += 1
                    continue

                match, was_created = Match.objects.get_or_create(
                    home=home,
                    away=away,
                    kickoff=fixture["kickoff"],
                )
                if was_created:
                    match.tags.add("world-cup", tournament)
                    created += 1
                else:
                    skipped += 1

            if dry_run:
                transaction.set_rollback(True)

        self.stdout.write(
            self.style.SUCCESS(
                f"Done. tournament={tournament}, parsed={len(fixtures)}, created={created}, "
                f"skipped={skipped}, placeholders={placeholders}, missing_clubs={missing}"
            )
        )
        if missing_teams:
            self.stdout.write(
                self.style.WARNING(
                    "Unknown teams (import clubs first): "
                    + ", ".join(sorted(missing_teams))
                )
            )

    def _download(self, group_path, knockout_path, tournament):
        group_path.parent.mkdir(parents=True, exist_ok=True)
        group_url, knockout_url = tournament_download_urls(tournament)
        self._download_file(group_url, group_path)
        self._download_file(knockout_url, knockout_path)

    def _download_file(self, url, destination):
        request = urllib.request.Request(
            url,
            headers={"User-Agent": "songbook-match-import/1.0"},
        )
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                destination.write_bytes(response.read())
        except urllib.error.URLError as exc:
            raise CommandError(f"Failed to download {url}: {exc}") from exc
        self.stdout.write(f"Downloaded {destination.name}")

    def _build_club_map(self):
        by_name = {club.name: club for club in Club.objects.all()}
        club_map = dict(by_name)
        for source_name, target_name in TEAM_ALIASES.items():
            club = by_name.get(target_name)
            if club is not None:
                club_map[source_name] = club
        return club_map


def parse_world_cup_fixtures(text, year=2026):
    fixtures = []
    current_date = None

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("=") or line.startswith("#") or line.startswith("▪"):
            continue
        if line.startswith("Group "):
            continue

        date_match = DATE_RE.match(line)
        if date_match:
            month_name, day = date_match.groups()
            month_key = month_name[:3] if month_name[:3] in MONTHS else month_name
            month = MONTHS.get(month_name) or MONTHS.get(month_key)
            if month is None:
                continue
            current_date = date(year, month, int(day))
            continue

        if current_date is None:
            continue

        match_line = MATCH_LINE_RE.match(raw_line)
        if not match_line:
            continue

        hour, minute, sign, offset_hours, teams_part = match_line.groups()
        offset = int(offset_hours) * (-1 if sign == "-" else 1)
        tz = timezone(timedelta(hours=offset))
        kickoff_time = time(int(hour), int(minute), tzinfo=tz)

        teams_part = teams_part.strip()
        if " v " in teams_part:
            home_name, away_name = teams_part.split(" v ", 1)
        else:
            score_match = SCORE_SPLIT_RE.match(teams_part)
            if not score_match:
                continue
            home_name, away_name = score_match.groups()

        home_name = home_name.strip()
        away_name = away_name.strip()
        kickoff = datetime.combine(current_date, kickoff_time).astimezone(LONDON)
        fixtures.append(
            {
                "home": home_name,
                "away": away_name,
                "kickoff": kickoff,
            }
        )

    return fixtures
