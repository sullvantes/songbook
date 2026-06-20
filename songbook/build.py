"""
Settings used only during Docker image build (collectstatic).

Not used at runtime on Fly — production uses songbook.production, which
sets ALLOWED_HOSTS from FLY_APP_NAME and fly secrets.
"""

from .settings import *  # noqa: F403

DEBUG = False
SECRET_KEY = "build-only-not-for-runtime"
ALLOWED_HOSTS = ["localhost"]
SITE_URL = "https://example.com"

DATABASES = {  # noqa: F811
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

STATIC_ROOT = BASE_DIR / "staticfiles"  # noqa: F405

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
