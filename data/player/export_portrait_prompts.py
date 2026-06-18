"""Export player portrait prompts for Cursor image generation batches.

Run from project root:
    python data/player/export_portrait_prompts.py --offset 0 --limit 50
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "songbook.settings")

import django

django.setup()

from django.db.models import Prefetch

from club.models import Club
from player.ai_portrait import build_portrait_prompt, portrait_context_for_player
from player.models import Player


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--limit", type=int, default=50)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parent / "portrait_prompt_batch.json",
    )
    args = parser.parse_args()

    players = list(
        Player.objects.order_by("name")
        .prefetch_related(Prefetch("clubs", queryset=Club.objects.order_by("name")))
        [args.offset : args.offset + args.limit]
    )

    payload = []
    for player in players:
        context = portrait_context_for_player(player)
        payload.append(
            {
                "slug": player.slug,
                "name": player.name,
                "prompt": build_portrait_prompt(context),
            }
        )

    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(payload)} prompts to {args.output}")


if __name__ == "__main__":
    main()
