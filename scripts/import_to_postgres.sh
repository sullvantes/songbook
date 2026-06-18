#!/usr/bin/env bash
# Load a JSON dump into the Postgres database used by docker compose.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
INPUT="${1:-$ROOT/data/sqlite_backup.json}"

cd "$ROOT"

if [ ! -f "$INPUT" ]; then
  echo "Backup file not found: $INPUT"
  echo "Run ./scripts/export_sqlite.sh first."
  exit 1
fi

if [ ! -f .env ]; then
  echo "Missing .env — run: cp .env.example .env"
  exit 1
fi

echo "Starting Postgres if needed..."
docker compose up -d db

echo "Running migrations..."
docker compose run --rm web python manage.py migrate --noinput

echo "Loading $INPUT ..."
RELATIVE_INPUT="${INPUT#"$ROOT"/}"
docker compose run --rm web python manage.py import_sqlite_backup --fixture "$RELATIVE_INPUT" --if-empty

echo "Done."
