#!/bin/sh
# Run when updating server
set -e
python -m pip install --upgrade pip
mkdir -p _data/media/
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate --noinput