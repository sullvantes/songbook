import json
import urllib.error
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError

from club.crest_utils import (
    attach_existing_crest_file,
    find_existing_crest_file,
    lookup_crest_url,
    save_club_crest,
)
from club.models import Club


class Command(BaseCommand):
    help = "Download and attach club crest images from JSON URLs or TheSportsDB."

    def add_arguments(self, parser):
        parser.add_argument(
            "json_file",
            nargs="?",
            type=str,
            help="Optional JSON file with club crest URLs.",
        )
        parser.add_argument(
            "--from-api",
            action="store_true",
            help="Look up missing crest URLs via TheSportsDB.",
        )
        parser.add_argument(
            "--update",
            action="store_true",
            help="Replace crests that are already set.",
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Report changes without downloading or saving files.",
        )
        parser.add_argument(
            "--attach-existing",
            action="store_true",
            help="Link crest files already on disk before downloading new ones.",
        )
        parser.add_argument(
            "--slug",
            type=str,
            help="Import crest for a single club slug only.",
        )
        parser.add_argument(
            "--pause",
            type=float,
            default=1.0,
            help="Seconds to wait between SportsDB API lookups (default: 1.0).",
        )
        parser.add_argument(
            "--limit",
            type=int,
            help="Process at most this many clubs.",
        )

    def handle(self, *args, **options):
        json_file = options.get("json_file")
        use_api = options["from_api"] or not json_file
        crest_map = self._load_crest_map(json_file) if json_file else {}

        queryset = Club.objects.order_by("name")
        if options["slug"]:
            queryset = queryset.filter(slug=options["slug"])
        if options["limit"]:
            queryset = queryset[: options["limit"]]

        clubs = list(queryset)
        if not clubs:
            raise CommandError("No clubs matched the requested filters.")

        imported = updated = attached = skipped = missing = failed = 0
        self.pause_seconds = options["pause"]
        attach_existing = options["attach_existing"] or not options["update"]

        for club in clubs:
            if club.crest and not options["update"]:
                skipped += 1
                self.stdout.write(f"Skipped (already has crest): {club.name}")
                continue

            if attach_existing and not club.crest:
                existing_path = find_existing_crest_file(club)
                if existing_path:
                    if options["dry_run"]:
                        self.stdout.write(
                            f"Would attach existing file: {club.name} -> {existing_path.name}"
                        )
                        attached += 1
                        continue

                    relative_path = attach_existing_crest_file(club)
                    attached += 1
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"Attached existing file: {club.name} -> {relative_path}"
                        )
                    )
                    continue

            crest_url, source = self._resolve_crest_url(club, crest_map, use_api)
            if not crest_url:
                missing += 1
                self.stdout.write(self.style.WARNING(f"No crest URL found: {club.name}"))
                continue

            action = "update" if club.crest else "import"
            if options["dry_run"]:
                self.stdout.write(f"Would {action}: {club.name} ({source}) -> {crest_url}")
                if action == "update":
                    updated += 1
                else:
                    imported += 1
                continue

            try:
                saved_path = save_club_crest(club, crest_url)
            except (OSError, ValueError, urllib.error.URLError, urllib.error.HTTPError) as exc:
                failed += 1
                self.stdout.write(self.style.ERROR(f"Failed: {club.name} ({exc})"))
                continue

            if action == "update":
                updated += 1
                self.stdout.write(self.style.WARNING(f"Updated: {club.name} -> {saved_path}"))
            else:
                imported += 1
                self.stdout.write(self.style.SUCCESS(f"Imported: {club.name} -> {saved_path}"))

        summary = (
            f"Done. imported={imported}, updated={updated}, attached={attached}, "
            f"skipped={skipped}, missing={missing}, failed={failed}"
        )
        if options["dry_run"]:
            summary = f"Dry run complete. {summary}"
        self.stdout.write(self.style.SUCCESS(summary))

    def _load_crest_map(self, json_file):
        json_path = Path(json_file).expanduser().resolve()
        if not json_path.is_file():
            raise CommandError(f"File not found: {json_path}")

        try:
            with json_path.open(encoding="utf-8") as handle:
                payload = json.load(handle)
        except json.JSONDecodeError as exc:
            raise CommandError(f"Invalid JSON in {json_path}: {exc}") from exc

        if isinstance(payload, list):
            records = payload
        elif isinstance(payload, dict) and isinstance(payload.get("clubs"), list):
            records = payload["clubs"]
        else:
            raise CommandError(
                "JSON must be a list of club objects or an object with a 'clubs' list."
            )

        crest_map = {}
        for index, item in enumerate(records, start=1):
            if not isinstance(item, dict):
                raise CommandError(
                    f"Record {index} must be a JSON object, got {type(item).__name__}."
                )
            crest_url = item.get("crest_url")
            if not crest_url:
                continue
            if item.get("slug"):
                crest_map[("slug", item["slug"])] = crest_url
            if item.get("name"):
                crest_map[("name", item["name"])] = crest_url

        return crest_map

    def _resolve_crest_url(self, club, crest_map, use_api):
        slug_key = ("slug", club.slug)
        name_key = ("name", club.name)
        if slug_key in crest_map:
            return crest_map[slug_key], "json"
        if name_key in crest_map:
            return crest_map[name_key], "json"
        if not use_api:
            return None, None

        try:
            match = lookup_crest_url(club.name, pause_seconds=self.pause_seconds)
        except urllib.error.HTTPError as exc:
            return None, f"api-error:{exc.code}"

        if not match:
            return None, None
        return match["crest_url"], f"api:{match['api_team']}"
