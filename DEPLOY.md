# Deployment Process

## General Development Testing:

To Initialize:
```
sh deploy.sh
```
set variables in .env
set config/settings/local_settings.py if needed

Create superuser:
```
python manage.py createsuperuser
```

When changing hostnames, find and replace it in all files as it is distributed in many locations.


## PythonAnywhere:

Expect this to take up to 50 CPU seconds.

\<user\> = PythonAnywhere username
\<project\> = Project Folder in PythonAnywhere

create folder at home/\<user\>/\<project\>/

create terminal at home/\<user\>/\<project\>/
```
git clone https://github.com/Multiplex64/Multiplex64_v2 .
mkvirtualenv --python=/usr/bin/python3.13 venv
```

set variables in .env
set config/settings/local_settings.py if needed

Go to PythonAnywhere app page and set static files:
/static/ ===== /home/\<user\>/\<project\>/_staticfiles

go to terminal at home/\<user\>/\<project\>/
```
sh deploy.sh
```

edit var/www/\<user\>_pythonanywhere_com_wsgi.py
```
import os
import sys
from dotenv import load_dotenv

base_dir = os.path.expanduser('~/\<project\>')
dotenv_path = os.path.join(base_dir, '.env')
load_dotenv(dotenv_path=dotenv_path)

## assuming your django settings file is at '/home/\<user\>/\<project\>/config/settings.py'
## and your manage.py is is at '/home/\<user\>/\<project\>/manage.py'
path = '/home/\<user\>/\<project\>'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

## then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```