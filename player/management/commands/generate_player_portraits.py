import time

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand, CommandError
from django.db.models import Prefetch

from club.models import Club
from player.ai_portrait import build_portrait_prompt, generate_with_retry, portrait_context_for_player
from player.models import Player


class Command(BaseCommand):
    help = "Generate retro video game player portraits using OpenAI image generation."

    def add_arguments(self, parser):
        parser.add_argument(
            "--update",
            action="store_true",
            help="Replace portraits that are already set.",
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Print prompts without calling OpenAI or saving files.",
        )
        parser.add_argument(
            "--slug",
            type=str,
            help="Generate a portrait for a single player slug.",
        )
        parser.add_argument(
            "--limit",
            type=int,
            help="Process at most this many players.",
        )
        parser.add_argument(
            "--pause",
            type=float,
            default=1.0,
            help="Seconds to wait between OpenAI requests (default: 1.0).",
        )

    def handle(self, *args, **options):
        queryset = Player.objects.order_by("name").prefetch_related(
            Prefetch("clubs", queryset=Club.objects.order_by("name"))
        )
        if options["slug"]:
            queryset = queryset.filter(slug=options["slug"])
        if options["limit"]:
            queryset = queryset[: options["limit"]]

        players = list(queryset)
        if not players:
            raise CommandError("No players matched the requested filters.")

        generated = skipped = failed = 0

        for index, player in enumerate(players, start=1):
            if player.portrait and not options["update"]:
                skipped += 1
                self.stdout.write(f"Skipped (already has portrait): {player.name}")
                continue

            prompt = build_portrait_prompt(portrait_context_for_player(player))
            if options["dry_run"]:
                self.stdout.write(self.style.WARNING(f"[dry-run] {player.name}"))
                self.stdout.write(prompt)
                self.stdout.write("")
                generated += 1
                continue

            try:
                png_data, _prompt = generate_with_retry(player)
            except Exception as exc:
                failed += 1
                self.stdout.write(self.style.ERROR(f"Failed: {player.name} ({exc})"))
                continue

            filename = f"{player.slug}.png"
            if player.portrait:
                player.portrait.delete(save=False)
            player.portrait.save(filename, ContentFile(png_data), save=True)
            generated += 1
            self.stdout.write(
                self.style.SUCCESS(
                    f"Generated ({index}/{len(players)}): {player.name} -> {player.portrait.name}"
                )
            )

            if options["pause"] and index < len(players):
                time.sleep(options["pause"])

        summary = f"Done. generated={generated}, skipped={skipped}, failed={failed}"
        if options["dry_run"]:
            summary = f"Dry run complete. {summary}"
        self.stdout.write(self.style.SUCCESS(summary))
