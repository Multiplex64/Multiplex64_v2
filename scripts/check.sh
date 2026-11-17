#!/bin/sh
# Make migrations and run tests before pushing
set -e
python manage.py makemigrations --noinput
./scripts/deploy.sh
python manage.py test