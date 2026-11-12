#!/bin/sh
# Run before pushing to git
set -e
python manage.py makemigrations --noinput
sh deploy.sh
python manage.py test
echo "Ready to commit and push to Git"