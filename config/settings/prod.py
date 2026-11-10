from .base import *
from django.core.exceptions import ImproperlyConfigured


def get_env_variable(var_name):
    """attempt to find env variable, raise error if misconfigured"""
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = (
            f"The environment variable '{var_name}' is required but was not found."
        )
        raise ImproperlyConfigured(error_msg)

DEBUG = False

# allowed hosts
ALLOWED_HOSTS = get_env_variable("ALLOWED_HOSTS").split(",")

# Keep the secret key used in production inside .env!
SECRET_KEY = get_env_variable("SECRET_KEY")

# Security settings
SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True