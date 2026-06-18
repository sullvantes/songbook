from pathlib import Path

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError

from club.models import Club

DEFAULT_FIXTURE = Path(settings.BASE_DIR) / "data" / "sqlite_backup.json"


class Command(BaseCommand):
    help = "Load data/sqlite_backup.json into the database."

    def add_arguments(self, parser):
        parser.add_argument(
            "--fixture",
            default=str(DEFAULT_FIXTURE),
            help="Path to JSON dump (default: data/sqlite_backup.json).",
        )
        parser.add_argument(
            "--if-empty",
            action="store_true",
            help="Skip import if the database already contains clubs.",
        )
        parser.add_argument(
            "--force",
            action="store_true",
            help="Load even when clubs already exist (may cause duplicate key errors).",
        )

    def handle(self, *args, **options):
        fixture = Path(options["fixture"]).resolve()
        if not fixture.is_file():
            raise CommandError(f"Fixture not found: {fixture}")

        if options["if_empty"] and Club.objects.exists():
            self.stdout.write("Database already has clubs; skipping import.")
            return

        if Club.objects.exists() and not options["force"]:
            raise CommandError(
                "Database already has data. Use --force to load anyway, "
                "or --if-empty to skip when data exists."
            )

        try:
            label = fixture.relative_to(Path(settings.BASE_DIR).resolve()).as_posix()
        except ValueError:
            label = str(fixture)

        self.stdout.write(f"Loading {label} ...")
        call_command("loaddata", label)
        self.stdout.write(self.style.SUCCESS("Import complete."))
