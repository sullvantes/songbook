import base64
import os
import time
import urllib.error
import urllib.request
from dataclasses import dataclass

from openai import OpenAI

## uses OPENAI to create a pixel art portrait
PORTRAIT_STYLE = """
Create a retro 16-bit SNES-style pixel art football player portrait for a character select screen.
Use this exact composition and visual style every time:
- chest-up bust, three-quarter angle, slight friendly expression
- ornate gold pixel art frame with dark blue inner border
- night stadium background with purple crowd tiers and bright white floodlights
- crisp visible pixels, rich dithered shading, limited color palette
- dramatic lighting from the upper left
- no text, no watermarks, no club crests, no sponsor logos
""".strip()

DEFAULT_MODEL = "dall-e-3"
DEFAULT_SIZE = "1024x1024"


@dataclass
class PlayerPortraitContext:
    name: str
    position: str
    club_name: str
    primary_color: str
    secondary_color: str


def _hex_to_rgb(value: str, fallback=(200, 16, 46)):
    value = (value or "").strip()
    if not value.startswith("#") or len(value) not in (4, 7):
        return fallback
    if len(value) == 4:
        value = "#" + "".join(ch * 2 for ch in value[1:])
    try:
        return tuple(int(value[i : i + 2], 16) for i in (1, 3, 5))
    except ValueError:
        return fallback


def _rgb_label(value: str, fallback: str) -> str:
    red, green, blue = _hex_to_rgb(value)
    return f"RGB({red}, {green}, {blue})"


def portrait_context_for_player(player) -> PlayerPortraitContext:
    clubs = list(player.clubs.all())
    branding = None
    for club in clubs:
        if club.primary_color:
            branding = club
            break
    if branding is None and clubs:
        branding = clubs[0]

    if branding is None:
        return PlayerPortraitContext(
            name=player.name,
            position=player.position or "footballer",
            club_name="generic club",
            primary_color="red",
            secondary_color="white",
        )

    return PlayerPortraitContext(
        name=player.name,
        position=player.position or "footballer",
        club_name=branding.name,
        primary_color=_rgb_label(branding.primary_color, "red"),
        secondary_color=_rgb_label(branding.secondary_color, "white"),
    )


def build_portrait_prompt(context: PlayerPortraitContext) -> str:
    return (
        f"{PORTRAIT_STYLE}\n\n"
        f"Subject: {context.name}, a {context.position}.\n"
        f"Kit inspired by {context.club_name}: {context.primary_color} shirt "
        f"with {context.secondary_color} collar or trim.\n"
        f"Make the likeness stylized but recognizable for {context.name}."
    )


def get_openai_client() -> OpenAI:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY is not set. Export it before running portrait generation."
        )
    return OpenAI(api_key=api_key)


def generate_ai_portrait(
    player,
    *,
    model: str | None = None,
    size: str = DEFAULT_SIZE,
    client: OpenAI | None = None,
) -> tuple[bytes, str]:
    context = portrait_context_for_player(player)
    prompt = build_portrait_prompt(context)
    client = client or get_openai_client()
    model = model or os.environ.get("OPENAI_IMAGE_MODEL", DEFAULT_MODEL)

    response = client.images.generate(
        model=model,
        prompt=prompt,
        size=size,
        response_format="b64_json",
        n=1,
    )
    image_data = response.data[0].b64_json
    if not image_data:
        raise RuntimeError("OpenAI returned no image data.")

    return base64.b64decode(image_data), prompt


def download_image_url(url: str, timeout: int = 60) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": "songbook-portrait-import/1.0"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        data = response.read()
    if not data:
        raise ValueError("Downloaded image is empty.")
    return data


def generate_with_retry(player, *, retries: int = 3, pause_seconds: float = 2.0, **kwargs) -> tuple[bytes, str]:
    last_error = None
    for attempt in range(retries):
        try:
            return generate_ai_portrait(player, **kwargs)
        except Exception as exc:
            last_error = exc
            if attempt < retries - 1:
                time.sleep(pause_seconds * (attempt + 1))
    raise last_error
