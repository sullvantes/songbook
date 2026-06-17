from django.core.management.base import BaseCommand
from django.db import transaction

from player.models import Player
from song.models import Song


class Command(BaseCommand):
    help = "Link songs to players when the song title exactly matches a player name."

    def add_arguments(self, parser):
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Report matches without writing to the database.",
        )
        parser.add_argument(
            "--force",
            action="store_true",
            help="Replace an existing player link when the title matches a different player.",
        )

    def handle(self, *args, **options):
        dry_run = options["dry_run"]
        force = options["force"]

        players_by_name = {player.name: player for player in Player.objects.all()}
        linked = skipped = already_linked = replaced = 0

        with transaction.atomic():
            for song in Song.objects.order_by("title"):
                player = players_by_name.get(song.title)
                if player is None:
                    continue

                if song.player_id == player.pk:
                    already_linked += 1
                    continue

                if song.player_id is not None and not force:
                    skipped += 1
                    self.stdout.write(
                        self.style.WARNING(
                            f"Skipped {song.title!r}: already linked to {song.player.name!r}"
                        )
                    )
                    continue

                action = "Would link" if dry_run else "Linked"
                if song.player_id is not None:
                    replaced += 1
                    action = "Would replace link for" if dry_run else "Replaced link for"

                self.stdout.write(f"{action}: {song.title!r} -> {player.name!r}")

                if not dry_run:
                    song.player = player
                    song.save(update_fields=["player"])

                linked += 1

            if dry_run:
                transaction.set_rollback(True)

        summary = (
            f"Done. linked={linked}, already_linked={already_linked}, "
            f"skipped={skipped}, replaced={replaced}"
        )
        if dry_run:
            summary = f"Dry run complete. {summary}"
        self.stdout.write(self.style.SUCCESS(summary))
