# PythonAnywhere Deployment

Expect this to take up to 50 CPU seconds.

## Initialize Web App

Create app if one doesn't exist, as manual configuration

Go to PythonAnywhere app page and set:

Working Directory:

`~/Multiplex64` (Should expland to `/home/<user>/Multiplex64`)

Virtualenv:

`venv` (Should expland to `/home/<user>/-virtualenvs/venv`)

Static files:

`/static/` ===== `/users/<username>/Multiplex64/_staticfiles/`


## Clear Existing Files

### Existing Site Stops Working Here!

Bash Terminal

```
pip freeze --user | xargs pip uninstall -y
rm -rf ~/*
rm -rf ~/.*
rm -rf /tmp/*
```

Open new console to regenerate files

## Deploy

Copy contents of [install.sh](install.sh) to `~/install.sh`

Bash Terminal

```
bash install.sh
```

When prompted:

Set variables in `.env`

Finish install.sh task to complete. The site should be running.

## To Update:

Bash Terminal at `~/Multiplex64/`

```
sh scripts/update.sh
```

Restart the web app
