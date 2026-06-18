"""Build a JSON crest URL map for clubs using TheSportsDB.

Run from project root:
    python data/club/generate_club_crest_urls.py
    python data/club/generate_club_crest_urls.py --write
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

from club.crest_utils import lookup_crest_url
from club.models import Club

OUTPUT = Path(__file__).resolve().parent / "club_crests.json"


def load_club_names_from_json():
    names = []
    for json_path in sorted(Path(__file__).resolve().parent.glob("*.json")):
        if json_path.name == "club_crests.json":
            continue
        with json_path.open(encoding="utf-8") as handle:
            payload = json.load(handle)
        records = payload if isinstance(payload, list) else payload.get("clubs", [])
        for item in records:
            if isinstance(item, dict) and item.get("name"):
                names.append(item["name"])
    return names


def collect_club_names():
    db_names = list(Club.objects.order_by("name").values_list("name", flat=True))
    if db_names:
        return db_names
    return sorted(set(load_club_names_from_json()))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write results to data/club/club_crests.json.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="Look up crest URLs for at most this many clubs.",
    )
    args = parser.parse_args()

    club_names = collect_club_names()
    if args.limit:
        club_names = club_names[: args.limit]

    results = []
    matched = 0

    for name in club_names:
        match = lookup_crest_url(name)
        record = {"name": name, "crest_url": None, "api_team": None, "score": None}
        if match:
            record.update(match)
            matched += 1
            print(f"OK  {name} -> {match['api_team']}")
        else:
            print(f"MISS {name}")
        results.append(record)

    print(f"\nMatched {matched}/{len(results)} clubs.")

    if args.write:
        with OUTPUT.open("w", encoding="utf-8") as handle:
            json.dump(results, handle, indent=2)
            handle.write("\n")
        print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
