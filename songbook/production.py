"""
Production settings for Fly.io and other hosts.

Set on Fly via fly.toml [env] or fly secrets set:
    DJANGO_SETTINGS_MODULE=songbook.production
    SECRET_KEY=...
    SITE_URL=https://your-app.fly.dev
    ALLOWED_HOSTS=your-app.fly.dev,yourdomain.com   (optional; .fly.dev added automatically)
"""

import os
from pathlib import Path
from urllib.parse import urlparse

from django.core.exceptions import ImproperlyConfigured

from songbook.database import config_from_database_url

from .settings import *  # noqa: F403


def env(name, default=None, *, required=False):
    value = os.environ.get(name, default)
    if required and not value:
        raise ImproperlyConfigured(f"Missing required environment variable: {name}")
    return value


def env_list(name, default=None, *, required=False):
    raw = env(name, default=default, required=required)
    if not raw:
        return []
    return [item.strip() for item in raw.split(",") if item.strip()]


DEBUG = False
SECRET_KEY = env("SECRET_KEY", required=True)

ALLOWED_HOSTS = env_list("ALLOWED_HOSTS")
FLY_APP_NAME = os.environ.get("FLY_APP_NAME")
if FLY_APP_NAME:
    ALLOWED_HOSTS.append(f"{FLY_APP_NAME}.fly.dev")
if not ALLOWED_HOSTS:
    raise ImproperlyConfigured("Set ALLOWED_HOSTS or deploy on Fly with FLY_APP_NAME.")

SITE_URL = env("SITE_URL", required=True).rstrip("/")
CSRF_TRUSTED_ORIGINS = env_list("CSRF_TRUSTED_ORIGINS")
if not CSRF_TRUSTED_ORIGINS:
    CSRF_TRUSTED_ORIGINS = [SITE_URL]
if FLY_APP_NAME and f"https://{FLY_APP_NAME}.fly.dev" not in CSRF_TRUSTED_ORIGINS:
    CSRF_TRUSTED_ORIGINS.append(f"https://{FLY_APP_NAME}.fly.dev")

# --- Database (Fly Postgres sets DATABASE_URL on attach) -----------------------

DATABASES = {  # noqa: F405
    "default": config_from_database_url(
        env("DATABASE_URL", required=True),
        conn_max_age=600,
    )
}

# --- Static / media ------------------------------------------------------------

STATIC_ROOT = BASE_DIR / "staticfiles"  # noqa: F405
MEDIA_ROOT = Path(env("MEDIA_ROOT", default=str(BASE_DIR / "media")))  # noqa: F405
SERVE_MEDIA = env("SERVE_MEDIA", default="false").lower() in {"1", "true", "yes"}

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
        "OPTIONS": {
            "location": MEDIA_ROOT,
            "base_url": MEDIA_URL,  # noqa: F405
        },
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

MIDDLEWARE.insert(  # noqa: F405
    MIDDLEWARE.index("django.middleware.security.SecurityMiddleware") + 1,  # noqa: F405
    "whitenoise.middleware.WhiteNoiseMiddleware",
)

# --- Email ---------------------------------------------------------------------

EMAIL_BACKEND = env(
    "EMAIL_BACKEND",
    default="django.core.mail.backends.smtp.EmailBackend",
)
DEFAULT_FROM_EMAIL = env(
    "DEFAULT_FROM_EMAIL",
    default=f"noreply@{urlparse(SITE_URL).hostname or 'localhost'}",
)

EMAIL_HOST = env("EMAIL_HOST", default="localhost")
EMAIL_PORT = int(env("EMAIL_PORT", default="587"))
EMAIL_HOST_USER = env("EMAIL_HOST_USER", default="")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD", default="")
EMAIL_USE_TLS = env("EMAIL_USE_TLS", default="true").lower() in {"1", "true", "yes"}

# --- Security (Fly terminates TLS at the edge) --------------------------------

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = env("SECURE_SSL_REDIRECT", default="true").lower() in {
    "1",
    "true",
    "yes",
}
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = int(env("SECURE_HSTS_SECONDS", default="31536000"))
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"
