#!/bin/sh
# Run tests on code
set -e
python manage.py makemigrations --check --dry-run
python manage.py test