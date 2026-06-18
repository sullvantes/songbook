import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from difflib import SequenceMatcher
from pathlib import Path

from django.conf import settings
from django.core.files.base import ContentFile

SPORTSDB_SEARCH_URL = "https://www.thesportsdb.com/api/v1/json/3/searchteams.php"
USER_AGENT = "songbook-crest-import/1.0"
NAME_SUFFIXES = (" United FC", " FC", " CF", " SC", " AFC")
NAME_PREFIXES = ("SS ", "SSC ", "ACF ", "AC ", "AS ", "RB ", "Borussia ")
CREST_UPLOAD_DIR = Path("clubs/crests")


def crest_media_dir():
    return Path(settings.MEDIA_ROOT) / CREST_UPLOAD_DIR


def find_existing_crest_file(club):
    matches = [
        path
        for path in crest_media_dir().glob(f"{club.slug}.*")
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg"}
    ]
    if not matches:
        return None
    matches.sort(key=lambda path: (len(path.name), path.name))
    return matches[0]


def attach_existing_crest_file(club):
    crest_file = find_existing_crest_file(club)
    if crest_file is None:
        return None

    relative_path = f"{CREST_UPLOAD_DIR.as_posix()}/{crest_file.name}"
    club.crest = relative_path
    club.save(update_fields=["crest"])
    return relative_path


def crest_search_terms(club_name):
    terms = []
    seen = set()

    def add(term):
        term = term.strip()
        if term and term not in seen:
            seen.add(term)
            terms.append(term)

    add(club_name)
    add(club_name.replace(" & ", " and "))

    for suffix in NAME_SUFFIXES:
        if club_name.endswith(suffix):
            add(club_name[: -len(suffix)])

    for prefix in NAME_PREFIXES:
        if club_name.startswith(prefix):
            add(club_name[len(prefix) :])

    return terms


def _name_similarity(left, right):
    left = re.sub(r"[^a-z0-9]+", " ", left.lower()).strip()
    right = re.sub(r"[^a-z0-9]+", " ", right.lower()).strip()
    return SequenceMatcher(None, left, right).ratio()


def fetch_sportsdb_teams(search_term, timeout=20, retries=3):
    query = urllib.parse.urlencode({"t": search_term})
    url = f"{SPORTSDB_SEARCH_URL}?{query}"
    last_error = None

    for attempt in range(retries):
        request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                payload = json.load(response)
            return payload.get("teams") or []
        except urllib.error.HTTPError as exc:
            last_error = exc
            if exc.code == 429 and attempt < retries - 1:
                time.sleep(2 ** attempt)
                continue
            raise

    if last_error:
        raise last_error
    return []


def pick_best_sportsdb_team(club_name, teams):
    soccer_teams = [team for team in teams if (team.get("strSport") or "").lower() == "soccer"]
    candidates = soccer_teams or teams

    ranked = []
    for team in candidates:
        badge_url = team.get("strBadge")
        if not badge_url:
            continue
        team_name = team.get("strTeam") or ""
        score = _name_similarity(club_name, team_name)
        ranked.append((score, team_name, badge_url, team))

    if not ranked:
        return None

    ranked.sort(key=lambda item: item[0], reverse=True)
    best_score, _, badge_url, team = ranked[0]
    if best_score < 0.55:
        return None
    return {
        "crest_url": badge_url,
        "api_team": team.get("strTeam"),
        "score": round(best_score, 3),
    }


def lookup_crest_url(club_name, pause_seconds=1.0):
    for term in crest_search_terms(club_name):
        teams = fetch_sportsdb_teams(term)
        match = pick_best_sportsdb_team(club_name, teams)
        if match:
            if pause_seconds:
                time.sleep(pause_seconds)
            return match
    if pause_seconds:
        time.sleep(pause_seconds)
    return None


def download_crest(url, timeout=30):
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        content_type = response.headers.get("Content-Type", "")
        data = response.read()

    if not data:
        raise ValueError("Downloaded crest file is empty.")

    extension = Path(urllib.parse.urlparse(url).path).suffix.lower()
    if extension not in {".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg"}:
        if "png" in content_type:
            extension = ".png"
        elif "jpeg" in content_type or "jpg" in content_type:
            extension = ".jpg"
        elif "webp" in content_type:
            extension = ".webp"
        elif "gif" in content_type:
            extension = ".gif"
        elif "svg" in content_type:
            extension = ".svg"
        else:
            extension = ".png"

    return data, extension


def save_club_crest(club, crest_url):
    data, extension = download_crest(crest_url)
    filename = f"{club.slug}{extension}"
    if club.crest:
        club.crest.delete(save=False)
    club.crest.save(filename, ContentFile(data), save=False)
    club.save(update_fields=["crest"])
    return club.crest.name
