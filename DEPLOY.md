# Deployment Process

This doc outlines a basic instruction set for deploying the project.

## General Development Testing:

Clone to local folder

To Initialize:

```
sh scripts/deploy.sh
```

set variables in `.env`

Create superuser:

```
python manage.py createsuperuser
```

Set sitemap URLs through administration!

When changing hostnames, find and replace it in all files as it is distributed in many locations.

## PythonAnywhere:

Expect this to take up to 50 CPU seconds.

### Clear Existing Files

Open Terminal

```
pip freeze --user | xargs pip uninstall -y
rm -rf ~/*
rm -rf ~/.*
rm -rf /tmp/*
```

Open new console to regenerate files

### Clone

Terminal at `~/`

```
mkvirtualenv --python=/usr/bin/python3.13 venv
git clone --depth 1 --branch prod --single-branch https://github.com/Multiplex64/Multiplex64_v2 Multiplex64
```

### Setup environment

set variables in `.env`

Go to PythonAnywhere app page and set static files:

`/static/` ===== `/users/<username>/Multiplex64/_staticfiles/`

### Deploy

Terminal at `~/Multiplex64/`

```
sh scripts/deploy.sh
```

edit `var/www/<username>_pythonanywhere_com_wsgi.py`

```
import os
import sys

path = os.path.expanduser('~/Multiplex64')
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### To Update:

Terminal at `~/Multiplex64/`

```
sh scripts/update.sh
```

Restart the web app
