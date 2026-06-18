#!/bin/bash
set -e

if [ -n "$DATABASE_URL" ]; then
  echo "Waiting for PostgreSQL..."
  until python - <<'PY'
import os
import sys
from urllib.parse import urlparse

import psycopg

parsed = urlparse(os.environ["DATABASE_URL"])
conninfo = (
    f"host={parsed.hostname} port={parsed.port or 5432} "
    f"dbname={parsed.path.lstrip('/')} user={parsed.username} "
    f"password={parsed.password}"
)
try:
    with psycopg.connect(conninfo, connect_timeout=3):
        pass
except Exception:
    sys.exit(1)
PY
  do
    sleep 1
  done
  echo "PostgreSQL is ready."
fi

# Avoid running migrate twice when the container command is already migrate.
if ! { [ "$1" = "python" ] && [ "$2" = "manage.py" ] && [ "$3" = "migrate" ]; }; then
  python manage.py migrate --noinput
fi

exec "$@"
