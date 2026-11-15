#!/bin/sh
# Run when updating server
set -e
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate --noinput
mkdir -p _data/media/