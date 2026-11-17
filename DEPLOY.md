# Deployment Process

This doc outlines a basic instruction set for deploying the project.

## General Development Testing:

Clone to local folder

To Initialize:

```
./scripts/setup.sh
```

set variables in `.env`

Create superuser:

```
python manage.py createsuperuser
```

Set sitemap URLs through administration!

When changing hostnames, find and replace it in all files as it is distributed in many locations.

## Platform Specific
[PythonAnywhere](deploy/pythonanywhere/DEPLOY.md)