# Football Chants Archive (Songbook)

A Django web app for browsing and collecting football fan chants and songs, linked to clubs, players, and matches.

## Features

- **Clubs** — browse clubs, view club-branded song lists, crests, and brand colors
- **Players** — player profiles with retro-style portraits, club links, and related songs
- **Songs & chants** — searchable archive with slug URLs, lyrics, tags, and media links
- **Matches** — log matches and link chants to specific games and minutes
- **Contributions** — registered users can suggest new songs (staff review via admin)
- **SEO** — meta descriptions, Open Graph tags, and canonical URLs

## Tech stack

- Python 3.12+
- Django 5.2
- SQLite (default)
- [django-taggit](https://github.com/jazzband/django-taggit) for tagging
- [django-unfold](https://github.com/unfoldadmin/django-unfold) for admin UI
- Pillow for image handling

## Getting started

### 1. Clone and create a virtual environment

```bash
git clone <your-repo-url>
cd songbook
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Run migrations

```bash
python manage.py migrate
```

### 3. Create a superuser (for admin access)

```bash
python manage.py createsuperuser
```

### 4. Run the development server

```bash
python manage.py runserver
```

Visit:

- **Home (clubs):** http://127.0.0.1:8000/
- **Admin:** http://127.0.0.1:8000/admin/

Uploaded images (crests, portraits, photos) are served from `/media/` in debug mode.

## Main URLs

| Path | Description |
|------|-------------|
| `/` | Club list (home) |
| `/clubs/` | Club list |
| `/clubs/<slug>/` | Songs for a club |
| `/players/` | Player list |
| `/players/?club=<slug>` | Players filtered by club |
| `/players/<slug>/` | Player detail |
| `/songs/` | Song list |
| `/songs/<slug>/` | Song detail |
| `/matches/` | Match list |
| `/matches/add/` | Add a match (login required) |
| `/matches/<id>/chants/add/` | Add a chant (login required) |

## Environment variables

| Variable | Purpose |
|----------|---------|
| `SITE_URL` | Canonical base URL for SEO tags (e.g. `https://example.com`) |
| `OPENAI_API_KEY` | Optional; used by `generate_player_portraits` for AI portrait generation |

## Management commands

Import and maintenance commands live under each app:

```bash
# Import clubs, players, and songs from JSON data files
python manage.py import_clubs data/clubs.json
python manage.py import_players data/players.json
python manage.py import_songs data/songs.json

# Club crests (from JSON URLs and/or TheSportsDB)
python manage.py import_club_crests --from-api
python manage.py import_club_crests --attach-existing

# Player portraits (from generated PNGs in data/player/portraits/generated/)
python manage.py import_player_portraits --update

# AI portrait generation (requires OPENAI_API_KEY)
python manage.py generate_player_portraits

# Export portrait prompts for batch image generation
python data/player/export_portrait_prompts.py --offset 0 --limit 50
```

## Project structure

```
songbook/          # Django project settings and root URLs
club/              # Club model, crest import, club song lists
player/            # Player model, portraits, player list/detail
song/              # Song model, search, suggest flow, SEO templates
chant/             # Match and Chant models
data/              # JSON import data and generated portrait assets
media/             # Uploaded crests, photos, and portraits (runtime)
```

## Development notes

- **Club colors** — set `primary_color` and `secondary_color` (hex) on clubs in admin; used on club and filtered player views.
- **Player portraits** — drop `{slug}.png` files in `data/player/portraits/generated/`, then run `import_player_portraits --update`.
- **Tags** — editable on clubs, players, songs, and matches via django-taggit in admin.

## License

Private project — add a license here if you plan to open-source it.
