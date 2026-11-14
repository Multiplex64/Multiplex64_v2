from pathlib import Path
import environ

BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(BASE_DIR / ".env")

env = environ.Env(
    ENV=(str, 'prod')
)

ENVIRONMENT = env("ENV")

if ENVIRONMENT == "dev":
    from .dev import *
else:
    from .prod import *
