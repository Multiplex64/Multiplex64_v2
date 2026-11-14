from pathlib import Path
import environ

BASE_DIR = Path(__file__).resolve().parent.parent

# Setup env variables
env = environ.Env(
    ENV=(str, "prod"),
)

environ.Env.read_env(BASE_DIR / ".env", overwrite=True)

ENVIRONMENT = env("ENV")

# Set setting values
if ENVIRONMENT == "dev":
    DEBUG = env.bool("DEBUG", default=True)
    SECURE_SSL_REDIRECT = env.bool("SECURE_SSL_REDIRECT", default=False)
    WHITENOISE_DISABLE = DEBUG and env.bool("WHITENOISE_DISABLE", default=True)
    ALLOWED_HOSTS = env.list(
        "ALLOWED_HOSTS", default=[".localhost", "127.0.0.1", "[::1]"]  # type: ignore[arg-type]
    )
    SECRET_KEY = env.str("SECRET_KEY", default="insecure-dev-key-never-use-in-prod")
    SECRET_DIR = env.str("SECRET_DIR", default="null/")
else:
    DEBUG = False
    SECURE_SSL_REDIRECT = True
    WHITENOISE_DISABLE = False
    ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
    SECRET_KEY = env.str("SECRET_KEY")
    SECRET_DIR = env.str("SECRET_DIR")

# Constants

SITE_ID = 1
ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "apps.home",
    "apps.tools",
    "apps.feedback",
    "apps.pricing",
]

# Middleware

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_ROOT = BASE_DIR / "_staticfiles"
WHITENOISE_ROOT = BASE_DIR / "static_root"
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# Disable whitenoise during development
if WHITENOISE_DISABLE:
    MIDDLEWARE.remove("whitenoise.middleware.WhiteNoiseMiddleware")
    STORAGES["staticfiles"] = {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage"
    }


# Email

MAILERS = {
    "default": {
        "BACKEND": "django.core.mail.backends.console.EmailBackend",
    },
}

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

# Security
if SECURE_SSL_REDIRECT:
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

    SECURE_HSTS_SECONDS = 31536000  # 1 year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
