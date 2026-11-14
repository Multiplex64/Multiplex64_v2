from .base import *
from django.core.exceptions import ImproperlyConfigured
import environ

BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env(
    ALLOWED_HOSTS=(list, ["localhost"]),
)

# allowed hosts
ALLOWED_HOSTS = env("ALLOWED_HOSTS")

# Keep the secret key used in production inside .env!
SECRET_KEY = env("SECRET_KEY")

# Security settings
SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "_data" / "db.sqlite3",
        "TIMEOUT": 20,  # Prevent immediate timeouts when locked
        "OPTIONS": {
            "init_command": (
                "PRAGMA journal_mode=WAL;"  # Enable concurrent reads during writes
                "PRAGMA synchronous=NORMAL;"  # Faster writes, completely safe with WAL
                "PRAGMA busy_timeout=5000;"  # Sleep and retry for up to 5s if locked
                "PRAGMA foreign_keys=ON;"  # Enforce foreign key constraints
                "PRAGMA temp_store=MEMORY;"  # Keep temporary tables and indices in RAM
                "PRAGMA mmap_size=134217728;"  # Memory-map up to 128 MB of the DB file to cut syscall overhead
                "PRAGMA journal_size_limit=67108864;"  # Cap the WAL file growth at 64 MB
                "PRAGMA cache_size=-20000;"  # Allocate ~20 MB page cache per connection
            ),
            "transaction_mode": "IMMEDIATE",  # Prevents deadlocks by locking early
        },
    }
}
