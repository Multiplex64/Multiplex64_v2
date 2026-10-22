import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENVIRONMENT = os.getenv("ENV", "prod")

if ENVIRONMENT == "dev":
    from .dev import *
else:
    from .prod import *

try:
    from .local_settings import *
except ImportError:
    pass