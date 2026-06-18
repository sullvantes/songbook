# Local development with Docker Compose

Run the app locally with **PostgreSQL** instead of SQLite.

## Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (or Docker Engine + Compose)

## Quick start

```bash
cp .env.example .env
docker compose up --build
```

Open **http://localhost:8000**

The entrypoint runs `migrate` automatically on startup.

Create an admin user (in another terminal):

```bash
docker compose exec web python manage.py createsuperuser
```

## What's running

| Service | Purpose | Port |
|---------|---------|------|
| `db` | PostgreSQL 16 | 5432 |
| `web` | Django dev server | 8000 |

Postgres credentials (from `.env.example`):

- Database: `songbook`
- User / password: `songbook`
- URL: `postgres://songbook:songbook@db:5432/songbook`

## Migrate existing SQLite data

If you have data in `db.sqlite3`, export it **before** setting `DATABASE_URL`:

```bash
unset DATABASE_URL   # ensure Django uses SQLite
./scripts/export_sqlite.sh
```

Start Postgres and import:

```bash
cp .env.example .env
docker compose up -d db
./scripts/import_to_postgres.sh
docker compose up web
```

Your `media/` folder is bind-mounted from the host, so crests and portraits stay in place.

## Common commands

```bash
docker compose up              # start db + web
docker compose up -d           # start in background
docker compose down            # stop containers
docker compose down -v         # stop and delete postgres volume (wipes DB)
docker compose logs -f web     # tail app logs
docker compose exec web python manage.py shell
docker compose exec web python manage.py import_clubs data/club/clubs.json
docker compose run --rm web python manage.py migrate
```

## Run Postgres only (Django on host)

Useful if you prefer `runserver` outside Docker but still want Postgres:

```bash
docker compose up -d db
export DATABASE_URL=postgres://songbook:songbook@localhost:5432/songbook
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Environment variables

See `.env.example`. Key vars:

| Variable | Local default |
|----------|---------------|
| `DATABASE_URL` | `postgres://songbook:songbook@db:5432/songbook` |
| `DEBUG` | `true` |
| `SERVE_MEDIA` | `true` (serve uploaded images) |
| `SITE_URL` | `http://localhost:8000` |

Without `DATABASE_URL`, `songbook.settings` falls back to SQLite for bare-metal dev.
