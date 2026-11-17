#!/bin/sh
# Make migrations and run tests before pushing
set -e
python manage.py makemigrations --noinput
sh scripts/deploy.sh
python manage.py test