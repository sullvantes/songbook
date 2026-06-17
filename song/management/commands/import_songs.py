import json
from pathlib import Path

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from club.models import Club
from player.models import Player
from song.models import Song

OPTIONAL_TEXT_FIELDS = ("lyrics", "description")
BOOLEAN_FIELDS = ("is_fan_chant", "accepted")


class Command(BaseCommand):
    help = "Import songs/chants from a JSON file and link them to clubs or players."

    def add_arguments(self, parser):
        parser.add_argument(
            "json_file",
            type=str,
            help="Path to a JSON file containing song records.",
        )
        parser.add_argument(
            "--user",
            type=str,
            help="Username to set as created_by for new songs (defaults to first superuser).",
        )
        parser.add_argument(
            "--update",
            action="store_true",
            help="Update existing songs matched by title instead of skipping them.",
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Validate and report changes without writing to the database.",
        )
        parser.add_argument(
            "--pending",
            action="store_true",
            help="Import songs with accepted=False instead of accepted=True.",
        )

    def handle(self, *args, **options):
        json_path = Path(options["json_file"]).expanduser().resolve()
        if not json_path.is_file():
            raise CommandError(f"File not found: {json_path}")

        songs_data = self._load_songs(json_path)
        update = options["update"]
        dry_run = options["dry_run"]
        default_accepted = not options["pending"]
        created_by = self._resolve_created_by(options["user"], dry_run)

        created = updated = skipped = 0

        with transaction.atomic():
            for index, item in enumerate(songs_data, start=1):
                if not isinstance(item, dict):
                    raise CommandError(
                        f"Record {index} must be a JSON object, got {type(item).__name__}."
                    )

                title = item.get("title")
                if not title:
                    raise CommandError(f"Record {index} is missing required field 'title'.")

                field_values = self._extract_field_values(item, default_accepted)
                tags = item["tags"] if "tags" in item else None
                club_names = self._club_names_from_item(item)
                clubs = self._resolve_clubs(index, title, club_names) if club_names else None
                player = self._resolve_player(index, title, item.get("player"))

                if tags is not None and not isinstance(tags, list):
                    raise CommandError(
                        f"Record {index} ({title}): 'tags' must be a list of strings."
                    )

                existing = Song.objects.filter(title=title).first()

                if existing and not update:
                    skipped += 1
                    self.stdout.write(f"Skipped existing song: {title}")
                    continue

                relation_parts = []
                if club_names:
                    relation_parts.append(", ".join(club_names))
                if player:
                    relation_parts.append(f"player {player.name}")
                relation = f" -> {'; '.join(relation_parts)}" if relation_parts else ""

                if dry_run:
                    action = "Would update" if existing else "Would create"
                    self.stdout.write(f"{action}: {title}{relation}")
                    if existing:
                        updated += 1
                    else:
                        created += 1
                    continue

                if existing:
                    for field, value in field_values.items():
                        setattr(existing, field, value)
                    existing.player = player
                    existing.save()
                    song = existing
                    updated += 1
                    self.stdout.write(self.style.WARNING(f"Updated: {title}"))
                else:
                    song = Song.objects.create(
                        title=title,
                        created_by=created_by,
                        player=player,
                        **field_values,
                    )
                    created += 1
                    self.stdout.write(self.style.SUCCESS(f"Created: {title}"))

                if tags is not None:
                    song.tags.set(tags)

                if clubs is not None:
                    song.clubs.set(clubs)
                    club_list = ", ".join(club.name for club in clubs)
                    self.stdout.write(f"  Linked clubs: {club_list}")

                if player:
                    self.stdout.write(f"  Linked player: {player.name}")

            if dry_run:
                transaction.set_rollback(True)

        summary = f"Done. created={created}, updated={updated}, skipped={skipped}"
        if dry_run:
            summary = f"Dry run complete. {summary}"
        self.stdout.write(self.style.SUCCESS(summary))

    def _load_songs(self, json_path):
        try:
            with json_path.open(encoding="utf-8") as handle:
                payload = json.load(handle)
        except json.JSONDecodeError as exc:
            raise CommandError(f"Invalid JSON in {json_path}: {exc}") from exc

        if isinstance(payload, list):
            return payload

        if isinstance(payload, dict) and isinstance(payload.get("songs"), list):
            return payload["songs"]

        raise CommandError(
            "JSON must be a list of song objects or an object with a 'songs' list."
        )

    def _club_names_from_item(self, item):
        if "clubs" in item:
            club_names = item["clubs"]
        elif "club" in item:
            club_names = [item["club"]]
        else:
            return None

        if not isinstance(club_names, list):
            raise CommandError("'clubs' must be a list of club names.")
        return club_names

    def _extract_field_values(self, item, default_accepted):
        values = {}
        for field in OPTIONAL_TEXT_FIELDS:
            if field not in item:
                continue
            value = item[field]
            values[field] = "" if value is None else value

        for field in BOOLEAN_FIELDS:
            if field in item:
                values[field] = bool(item[field])
            elif field == "accepted":
                values[field] = default_accepted
            elif field == "is_fan_chant":
                values[field] = True

        return values

    def _resolve_created_by(self, username, dry_run):
        if username:
            try:
                return User.objects.get(username=username)
            except User.DoesNotExist as exc:
                raise CommandError(f"User not found: {username}") from exc

        user = User.objects.filter(is_superuser=True).order_by("pk").first()
        if user:
            return user

        if dry_run:
            return None

        raise CommandError(
            "No superuser found to assign as created_by. Create one or pass --user."
        )

    def _resolve_clubs(self, index, title, club_names):
        clubs = []
        missing = []

        for club_name in club_names:
            if not club_name:
                raise CommandError(
                    f"Record {index} ({title}): club names must be non-empty strings."
                )

            club = Club.objects.filter(name=club_name).first()
            if club is None:
                missing.append(club_name)
            else:
                clubs.append(club)

        if missing:
            missing_list = ", ".join(missing)
            raise CommandError(
                f"Record {index} ({title}): unknown club(s): {missing_list}. "
                "Import clubs first or check the names match exactly."
            )

        return clubs

    def _resolve_player(self, index, title, player_name):
        if player_name is None:
            return None
        if not player_name:
            raise CommandError(
                f"Record {index} ({title}): 'player' must be a non-empty string."
            )

        player = Player.objects.filter(name=player_name).first()
        if player is None:
            raise CommandError(
                f"Record {index} ({title}): unknown player {player_name!r}. "
                "Import players first or check the name matches exactly."
            )
        return player
