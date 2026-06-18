# Deploy to Fly.io

This guide gets the Football Chants Archive running on [Fly.io](https://fly.io) with PostgreSQL and persistent media storage.

## Prerequisites

- A [Fly.io account](https://fly.io/app/sign-up)
- The [Fly CLI](https://fly.io/docs/hands-on/install-flyctl/) installed
- This repo cloned locally

```bash
brew install flyctl   # macOS
fly auth login
```

## 1. Create the Fly app

From the project root:

```bash
cd songbook
fly launch --no-deploy
```

When prompted:

- **App name** — accept `songbook` or pick your own (update `app` in `fly.toml` to match)
- **Region** — pick one close to you (e.g. `lhr` for London)
- **PostgreSQL** — say **no** for now (we attach it in the next step)
- **Redis** — no

`fly launch` uses the existing `Dockerfile` and `fly.toml`.

## 2. Add PostgreSQL

```bash
fly postgres create --name songbook-db --region lhr
fly postgres attach songbook-db
```

This sets the `DATABASE_URL` secret on your app automatically.

## 3. Add a volume for uploaded media

Crests and player portraits need persistent disk (containers are ephemeral):

```bash
fly volumes create media_data --region lhr --size 1
```

The volume mounts at `/data`; `MEDIA_ROOT` is `/data/media` in `fly.toml`.

## 4. Set secrets

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copy the output, then:

```bash
fly secrets set \
  SECRET_KEY="paste-your-secret-key-here" \
  SITE_URL="https://songbook.fly.dev"
```

Replace `songbook` with your actual app name if different.

Optional custom domain:

```bash
fly secrets set ALLOWED_HOSTS="songbook.fly.dev,yourdomain.com"
```

## 5. Deploy

```bash
fly deploy
```

Fly will build the Docker image, run migrations (`release_command` in `fly.toml`), and start the app.

Visit: **https://your-app-name.fly.dev**

## 6. Create an admin user

```bash
fly ssh console -C "python manage.py createsuperuser"
```

## 7. Load your data (optional)

If `data/sqlite_backup.json` is in the repo, it is **imported automatically on deploy** when the database has no clubs yet (`scripts/fly_release.sh` runs `migrate` then `import_sqlite_backup --if-empty`).

Export from local SQLite first:

```bash
unset DATABASE_URL
./scripts/export_sqlite.sh   # writes data/sqlite_backup.json
```

Commit the file (or ensure it is included in the Docker build), then deploy:

```bash
fly deploy
```

Subsequent deploys skip import if clubs already exist. To force a reload:

```bash
fly ssh console -C "python manage.py import_sqlite_backup --force"
```

For media files (crests, portraits), copy them to the volume:

```bash
# from your machine, with media/ populated locally:
fly ssh sftp shell
put -r media/* /data/media/
```

Or re-run your import commands on the server:

```bash
fly ssh console
python manage.py import_clubs data/club/clubs.json
python manage.py import_player_portraits --update
```

## Email (account activation)

By default production uses SMTP. For a real site, set mail secrets (example with Resend/SMTP):

```bash
fly secrets set \
  EMAIL_HOST="smtp.resend.com" \
  EMAIL_PORT="587" \
  EMAIL_HOST_USER="resend" \
  EMAIL_HOST_PASSWORD="your-api-key" \
  DEFAULT_FROM_EMAIL="noreply@yourdomain.com"
```

## Useful commands

```bash
fly status              # app health
fly logs                # live logs
fly ssh console         # shell on the running machine
fly postgres connect -a songbook-db   # psql to the database
fly secrets list        # view secret names (not values)
```

## Custom domain

```bash
fly certs add yourdomain.com
fly secrets set SITE_URL="https://yourdomain.com" ALLOWED_HOSTS="yourdomain.com,www.yourdomain.com"
```

Point DNS at Fly as shown by `fly certs show yourdomain.com`.

## Cost estimate

- **App machine** — ~$0–5/mo (can auto-stop when idle)
- **PostgreSQL** — ~$2–7/mo for smallest plan
- **Volume (1 GB)** — ~$0.15/mo

See [Fly.io pricing](https://fly.io/docs/about/pricing/).

## Troubleshooting

**Deploy fails on migrate** — ensure Postgres is attached: `fly secrets list` should show `DATABASE_URL`.

**502 / health check fails** — check `fly logs`. Confirm `SECRET_KEY` and `SITE_URL` are set.

**Images missing** — confirm the volume exists (`fly volumes list`) and media files are under `/data/media` on the machine.

**Static files broken** — `collectstatic` runs during Docker build; redeploy after template/CSS changes.
