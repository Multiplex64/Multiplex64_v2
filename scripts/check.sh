#!/bin/sh
# Make migrations and run tests before pushing
set -e
./scripts/deploy.sh
python manage.py check --deploy --fail-level WARNING
python manage.py makemigrations --check --dry-run
python manage.py test