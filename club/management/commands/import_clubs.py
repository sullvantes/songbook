import json
import re
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from club.models import Club

OPTIONAL_TEXT_FIELDS = (
    "nickname",
    "stadium",
    "location",
    "website",
    "primary_color",
    "secondary_color",
)
HEX_COLOR_RE = re.compile(r"^#(?:[0-9a-fA-F]{3}){1,2}$")


class Command(BaseCommand):
    help = "Import clubs from a JSON file."

    def add_arguments(self, parser):
        parser.add_argument(
            "json_file",
            type=str,
            help="Path to a JSON file containing club records.",
        )
        parser.add_argument(
            "--update",
            action="store_true",
            help="Update existing clubs matched by name instead of skipping them.",
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Validate and report changes without writing to the database.",
        )

    def handle(self, *args, **options):
        json_path = Path(options["json_file"]).expanduser().resolve()
        if not json_path.is_file():
            raise CommandError(f"File not found: {json_path}")

        clubs_data = self._load_clubs(json_path)
        update = options["update"]
        dry_run = options["dry_run"]

        created = updated = skipped = 0

        with transaction.atomic():
            for index, item in enumerate(clubs_data, start=1):
                if not isinstance(item, dict):
                    raise CommandError(
                        f"Record {index} must be a JSON object, got {type(item).__name__}."
                    )

                name = item.get("name")
                if not name:
                    raise CommandError(f"Record {index} is missing required field 'name'.")

                field_values = self._extract_field_values(item)
                self._validate_colors(index, name, field_values)
                tags = item["tags"] if "tags" in item else None

                if tags is not None and not isinstance(tags, list):
                    raise CommandError(
                        f"Record {index} ({name}): 'tags' must be a list of strings."
                    )

                existing = Club.objects.filter(name=name).first()

                if existing and not update:
                    skipped += 1
                    self.stdout.write(f"Skipped existing club: {name}")
                    continue

                if dry_run:
                    action = "Would update" if existing else "Would create"
                    self.stdout.write(f"{action}: {name}")
                    if existing:
                        updated += 1
                    else:
                        created += 1
                    continue

                if existing:
                    for field, value in field_values.items():
                        setattr(existing, field, value)
                    existing.save()
                    club = existing
                    updated += 1
                    self.stdout.write(self.style.WARNING(f"Updated: {name}"))
                else:
                    club = Club.objects.create(name=name, **field_values)
                    created += 1
                    self.stdout.write(self.style.SUCCESS(f"Created: {name}"))

                if tags is not None:
                    club.tags.set(tags)

            if dry_run:
                transaction.set_rollback(True)

        summary = f"Done. created={created}, updated={updated}, skipped={skipped}"
        if dry_run:
            summary = f"Dry run complete. {summary}"
        self.stdout.write(self.style.SUCCESS(summary))

    def _load_clubs(self, json_path):
        try:
            with json_path.open(encoding="utf-8") as handle:
                payload = json.load(handle)
        except json.JSONDecodeError as exc:
            raise CommandError(f"Invalid JSON in {json_path}: {exc}") from exc

        if isinstance(payload, list):
            return payload

        if isinstance(payload, dict) and isinstance(payload.get("clubs"), list):
            return payload["clubs"]

        raise CommandError(
            "JSON must be a list of club objects or an object with a 'clubs' list."
        )

    def _extract_field_values(self, item):
        values = {}
        for field in OPTIONAL_TEXT_FIELDS:
            if field not in item:
                continue
            value = item[field]
            values[field] = "" if value is None else value

        if "founded" in item:
            values["founded"] = item["founded"]

        if "slug" in item:
            values["slug"] = item["slug"]

        return values

    def _validate_colors(self, index, name, field_values):
        for field in ("primary_color", "secondary_color"):
            value = field_values.get(field)
            if value and not HEX_COLOR_RE.match(value):
                raise CommandError(
                    f"Record {index} ({name}): '{field}' must be a hex color (e.g. #C8102E)."
                )
