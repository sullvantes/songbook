import shutil
from pathlib import Path

from django.conf import settings
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand, CommandError
from django.db.models import Prefetch

from club.models import Club
from player.models import Player

DEFAULT_SOURCE_DIR = Path(settings.BASE_DIR) / "data" / "player" / "portraits" / "generated"


class Command(BaseCommand):
    help = "Import Cursor-generated portrait PNGs from data/player/portraits/generated/."

    def add_arguments(self, parser):
        parser.add_argument(
            "--source-dir",
            type=str,
            default=str(DEFAULT_SOURCE_DIR),
            help="Directory containing <player-slug>.png files.",
        )
        parser.add_argument(
            "--update",
            action="store_true",
            help="Replace portraits that are already set.",
        )
        parser.add_argument(
            "--slug",
            type=str,
            help="Import a portrait for a single player slug.",
        )
        parser.add_argument(
            "--limit",
            type=int,
            help="Import at most this many portraits.",
        )

    def handle(self, *args, **options):
        source_dir = Path(options["source_dir"]).expanduser().resolve()
        if not source_dir.is_dir():
            raise CommandError(f"Source directory not found: {source_dir}")

        queryset = Player.objects.order_by("name").prefetch_related(
            Prefetch("clubs", queryset=Club.objects.order_by("name"))
        )
        if options["slug"]:
            queryset = queryset.filter(slug=options["slug"])
        if options["limit"]:
            queryset = queryset[: options["limit"]]

        imported = skipped = missing = failed = 0

        for player in queryset:
            if player.portrait and not options["update"]:
                skipped += 1
                continue

            source_file = source_dir / f"{player.slug}.png"
            if not source_file.is_file():
                missing += 1
                continue

            try:
                png_data = source_file.read_bytes()
                if not png_data:
                    raise ValueError("Portrait file is empty.")
            except OSError as exc:
                failed += 1
                self.stdout.write(self.style.ERROR(f"Failed to read {source_file}: {exc}"))
                continue

            filename = f"{player.slug}.png"
            if player.portrait:
                player.portrait.delete(save=False)
            player.portrait.save(filename, ContentFile(png_data), save=True)
            imported += 1
            self.stdout.write(
                self.style.SUCCESS(f"Imported: {player.name} -> {player.portrait.name}")
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"Done. imported={imported}, skipped={skipped}, missing={missing}, failed={failed}"
            )
        )
