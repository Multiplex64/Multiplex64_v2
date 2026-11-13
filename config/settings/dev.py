from .base import *

ALLOWED_HOSTS = [".localhost", "127.0.0.1", "[::1]"]
SECRET_KEY = "insecure-dev-key-never-use-in-prod"

if DEBUG:
    MIDDLEWARE.remove("whitenoise.middleware.WhiteNoiseMiddleware")
    STORAGES["staticfiles"] = {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage"
    }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "_data" / "db.sqlite3",
    }
}