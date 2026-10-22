from .base import *
DEBUG = os.getenv("DEBUG", 'True') == "True"
ALLOWED_HOSTS = ['.localhost', '127.0.0.1', '[::1]']
SECRET_KEY = "insecure-dev-key-never-use-in-prod"