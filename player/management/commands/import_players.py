import json
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from club.models import Club
from player.models import Player

OPTIONAL_TEXT_FIELDS = ("position", "years_active")


class Command(BaseCommand):
    help = "Import players from a JSON file and link them to clubs."

    def add_arguments(self, parser):
        parser.add_argument(
            "json_file",
            type=str,
            help="Path to a JSON file containing player records.",
        )
        parser.add_argument(
            "--update",
            action="store_true",
            help="Update existing players matched by name instead of skipping them.",
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

        players_data = self._load_players(json_path)
        update = options["update"]
        dry_run = options["dry_run"]

        created = updated = skipped = 0

        with transaction.atomic():
            for index, item in enumerate(players_data, start=1):
                if not isinstance(item, dict):
                    raise CommandError(
                        f"Record {index} must be a JSON object, got {type(item).__name__}."
                    )

                name = item.get("name")
                if not name:
                    raise CommandError(f"Record {index} is missing required field 'name'.")

                field_values = self._extract_field_values(item)
                tags = item["tags"] if "tags" in item else None
                club_names = item["clubs"] if "clubs" in item else None

                if tags is not None and not isinstance(tags, list):
                    raise CommandError(
                        f"Record {index} ({name}): 'tags' must be a list of strings."
                    )

                if club_names is not None and not isinstance(club_names, list):
                    raise CommandError(
                        f"Record {index} ({name}): 'clubs' must be a list of club names."
                    )

                clubs = self._resolve_clubs(index, name, club_names) if club_names else None

                existing = Player.objects.filter(name=name).first()

                if existing and not update:
                    skipped += 1
                    self.stdout.write(f"Skipped existing player: {name}")
                    continue

                if dry_run:
                    action = "Would update" if existing else "Would create"
                    club_info = f" -> {', '.join(club_names)}" if club_names else ""
                    self.stdout.write(f"{action}: {name}{club_info}")
                    if existing:
                        updated += 1
                    else:
                        created += 1
                    continue

                if existing:
                    for field, value in field_values.items():
                        setattr(existing, field, value)
                    existing.save()
                    player = existing
                    updated += 1
                    self.stdout.write(self.style.WARNING(f"Updated: {name}"))
                else:
                    player = Player.objects.create(name=name, **field_values)
                    created += 1
                    self.stdout.write(self.style.SUCCESS(f"Created: {name}"))

                if tags is not None:
                    player.tags.set(tags)

                if clubs is not None:
                    player.clubs.set(clubs)
                    club_list = ", ".join(club.name for club in clubs)
                    self.stdout.write(f"  Linked clubs: {club_list}")

            if dry_run:
                transaction.set_rollback(True)

        summary = f"Done. created={created}, updated={updated}, skipped={skipped}"
        if dry_run:
            summary = f"Dry run complete. {summary}"
        self.stdout.write(self.style.SUCCESS(summary))

    def _load_players(self, json_path):
        try:
            with json_path.open(encoding="utf-8") as handle:
                payload = json.load(handle)
        except json.JSONDecodeError as exc:
            raise CommandError(f"Invalid JSON in {json_path}: {exc}") from exc

        if isinstance(payload, list):
            return payload

        if isinstance(payload, dict) and isinstance(payload.get("players"), list):
            return payload["players"]

        raise CommandError(
            "JSON must be a list of player objects or an object with a 'players' list."
        )

    def _extract_field_values(self, item):
        values = {}
        for field in OPTIONAL_TEXT_FIELDS:
            if field not in item:
                continue
            value = item[field]
            values[field] = "" if value is None else value
        return values

    def _resolve_clubs(self, index, player_name, club_names):
        clubs = []
        missing = []

        for club_name in club_names:
            if not club_name:
                raise CommandError(
                    f"Record {index} ({player_name}): club names must be non-empty strings."
                )

            club = Club.objects.filter(name=club_name).first()
            if club is None:
                missing.append(club_name)
            else:
                clubs.append(club)

        if missing:
            missing_list = ", ".join(missing)
            raise CommandError(
                f"Record {index} ({player_name}): unknown club(s): {missing_list}. "
                "Import clubs first or check the names match exactly."
            )

        return clubs
