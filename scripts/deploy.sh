#!/bin/sh
# Run when updating server
set -e
mkdir -p _data/{media,logs}/
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate --noinput