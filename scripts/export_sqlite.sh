#!/usr/bin/env bash
# Export data from the local SQLite database (run before switching to Postgres).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUTPUT="${1:-$ROOT/data/sqlite_backup.json}"

cd "$ROOT"

if [ -n "${DATABASE_URL:-}" ]; then
  echo "Unset DATABASE_URL first so Django uses SQLite."
  echo "  unset DATABASE_URL"
  exit 1
fi

if [ ! -f db.sqlite3 ]; then
  echo "No db.sqlite3 found at $ROOT/db.sqlite3"
  exit 1
fi

echo "Exporting SQLite data to $OUTPUT"
python manage.py dumpdata \
  --natural-foreign \
  --natural-primary \
  -e contenttypes \
  -e auth.Permission \
  --indent 2 \
  > "$OUTPUT"

echo "Done. $(wc -l < "$OUTPUT") lines written."
