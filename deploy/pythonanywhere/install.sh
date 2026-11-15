#!/bin/bash
set -e
cd ~/
SCRIPT_PATH="$(realpath "$0")"
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=$(which python3)
source "$(which virtualenvwrapper.sh)"
# Clone repo
echo "Creating venv"
mkvirtualenv --python=/usr/bin/python3.13 venv
echo "Cloning Repo"
git clone --depth 1 --branch prod --single-branch https://github.com/Multiplex64/Multiplex64_v2 Multiplex64
read -p "Create .env file, set working directory, venv setting, and static directory. Then, press ENTER."
echo ""
# Run setup script
cd ~/Multiplex64
echo "Setting Up Website"
sh scripts/setup.sh
# Set wsgi
echo "Setting WSGI"
cp ~/Multiplex64/config/wsgi.py "/var/www/${USER}_pythonanywhere_com_wsgi.py"
# Restart server
echo "Starting Server"
touch "/var/www/${USER}_pythonanywhere_com_wsgi.py"
rm -- SCRIPT_PATH