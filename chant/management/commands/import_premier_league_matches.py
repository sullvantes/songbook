import re
import urllib.error
import urllib.request
from datetime import date, datetime, time
from pathlib import Path
from zoneinfo import ZoneInfo

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from club.models import Club
from chant.models import Match

DEFAULT_SEASON = "2025-26"
LONDON = ZoneInfo("Europe/London")

DATE_RE = re.compile(
    r"^(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun)\s+"
    r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+"
    r"(\d{1,2})(?:\s+(\d{4}))?$"
)
TIME_RE = re.compile(r"^(\d{1,2}):(\d{2})\s+")
SCORE_SUFFIX_RE = re.compile(r"\s+\d+-\d+(?:\s+\(\d+-\d+\))?$")

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
}

# OpenFootball team names -> club names in this project.
TEAM_ALIASES = {
    "Manchester United FC": "Manchester United",
    "Manchester City FC": "Manchester City",
    "Tottenham Hotspur FC": "Tottenham Hotspur",
    "Wolverhampton Wanderers FC": "Wolverhampton Wanderers",
    "Newcastle United FC": "Newcastle United",
    "West Ham United FC": "West Ham United",
    "Brighton & Hove Albion FC": "Brighton & Hove Albion",
    "Nottingham Forest FC": "Nottingham Forest",
    "Aston Villa FC": "Aston Villa",
    "Leicester City FC": "Leicester City",
    "Southampton FC": "Southampton FC",
    "Arsenal FC": "Arsenal FC",
    "Chelsea FC": "Chelsea FC",
    "Everton FC": "Everton FC",
    "Liverpool FC": "Liverpool FC",
    "AFC Bournemouth": "AFC Bournemouth",
    "Brentford FC": "Brentford FC",
    "Crystal Palace FC": "Crystal Palace FC",
    "Fulham FC": "Fulham FC",
    "Ipswich Town FC": "Ipswich Town FC",
    "Leeds United FC": "Leeds United",
    "Sunderland AFC": "Sunderland AFC",
    "Burnley FC": "Burnley FC",
}


def season_source_path(season):
    return Path(settings.BASE_DIR) / "data" / "match" / f"premier_league_{season}.txt"


def season_download_url(season):
    return (
        "https://raw.githubusercontent.com/openfootball/england/master/"
        f"{season}/1-premierleague.txt"
    )


def season_start_year(season):
    return int(season.split("-", 1)[0])


class Command(BaseCommand):
    help = "Import Premier League fixtures from OpenFootball text format."

    def add_arguments(self, parser):
        parser.add_argument(
            "--season",
            type=str,
            default=DEFAULT_SEASON,
            help="Season folder/tag (e.g. 2025-26).",
        )
        parser.add_argument(
            "--source",
            type=str,
            help="Path to fixture text file (defaults to data/match/premier_league_<season>.txt).",
        )
        parser.add_argument(
            "--download",
            action="store_true",
            help="Download the fixture file from OpenFootball before importing.",
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Parse and report without writing to the database.",
        )

    def handle(self, *args, **options):
        season = options["season"]
        source_path = Path(
            options["source"] or season_source_path(season)
        ).expanduser().resolve()

        if options["download"]:
            self._download(source_path, season)

        if not source_path.is_file():
            raise CommandError(
                f"Fixture file not found: {source_path}. "
                "Run with --download or place the file manually."
            )

        fixtures = parse_openfootball_fixtures(
            source_path.read_text(encoding="utf-8"),
            default_year=season_start_year(season),
        )
        if not fixtures:
            raise CommandError(f"No fixtures parsed from {source_path}.")

        club_map = self._build_club_map()
        created = skipped = missing = 0
        missing_teams = set()
        dry_run = options["dry_run"]

        with transaction.atomic():
            for fixture in fixtures:
                home = club_map.get(fixture["home"])
                away = club_map.get(fixture["away"])
                if home is None:
                    missing_teams.add(fixture["home"])
                    missing += 1
                    continue
                if away is None:
                    missing_teams.add(fixture["away"])
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
                    match.tags.add("premier-league", season)
                    created += 1
                else:
                    skipped += 1

            if dry_run:
                transaction.set_rollback(True)

        self.stdout.write(
            self.style.SUCCESS(
                f"Done. season={season}, parsed={len(fixtures)}, created={created}, "
                f"skipped={skipped}, missing_clubs={missing}"
            )
        )
        if missing_teams:
            self.stdout.write(
                self.style.WARNING(
                    "Unknown teams (import clubs first): "
                    + ", ".join(sorted(missing_teams))
                )
            )

    def _download(self, destination, season):
        destination.parent.mkdir(parents=True, exist_ok=True)
        request = urllib.request.Request(
            season_download_url(season),
            headers={"User-Agent": "songbook-match-import/1.0"},
        )
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                destination.write_bytes(response.read())
        except urllib.error.URLError as exc:
            raise CommandError(f"Failed to download fixtures: {exc}") from exc
        self.stdout.write(f"Downloaded fixtures to {destination}")

    def _build_club_map(self):
        clubs = Club.objects.all()
        by_name = {club.name: club for club in clubs}
        club_map = {}
        for source_name, target_name in TEAM_ALIASES.items():
            club = by_name.get(target_name)
            if club is not None:
                club_map[source_name] = club
        return club_map


def parse_openfootball_fixtures(text, default_year=2025):
    fixtures = []
    current_year = default_year
    current_date = None

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("=") or line.startswith("#") or line.startswith("▪"):
            continue

        date_match = DATE_RE.match(line)
        if date_match:
            month_name, day, year = date_match.groups()
            if year:
                current_year = int(year)
            current_date = date(current_year, MONTHS[month_name], int(day))
            continue

        if " v " not in raw_line or current_date is None:
            continue

        kickoff_time = time(15, 0)
        remainder = raw_line.strip()
        time_match = TIME_RE.match(remainder)
        if time_match:
            kickoff_time = time(int(time_match.group(1)), int(time_match.group(2)))
            remainder = remainder[time_match.end() :]

        home_name, away_part = remainder.split(" v ", 1)
        away_name = SCORE_SUFFIX_RE.sub("", away_part).strip()
        home_name = home_name.strip()

        kickoff = datetime.combine(current_date, kickoff_time, tzinfo=LONDON)
        fixtures.append(
            {
                "home": home_name,
                "away": away_name,
                "kickoff": kickoff,
            }
        )

    return fixtures
