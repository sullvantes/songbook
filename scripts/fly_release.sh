#!/bin/bash
set -euo pipefail

python manage.py migrate --noinput

if [ -f data/sqlite_backup.json ]; then
  python manage.py import_sqlite_backup --if-empty
else
  echo "No data/sqlite_backup.json found; skipping data import."
fi
