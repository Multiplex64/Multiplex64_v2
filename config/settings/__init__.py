import os

ENVIRONMENT = os.getenv("ENV", "prod")

if ENVIRONMENT == "dev":
    from .dev import *
else:
    from .prod import *
