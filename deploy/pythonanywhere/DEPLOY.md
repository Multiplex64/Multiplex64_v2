# PythonAnywhere Deployment

Expect this to take up to 50 CPU seconds.

## Clear Existing Files

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
sh install.sh
```

When prompted:

Set variables in `.env`

Go to PythonAnywhere app page and set static files:

`/static/` ===== `/users/<username>/Multiplex64/_staticfiles/`

Finish install.sh task to complete.

## To Update:

Bash Terminal at `~/Multiplex64/`

```
sh scripts/update.sh
```

Restart the web app