#!/bin/sh
# Run when cloning and initializing repository
sh deploy.sh
git config core.hooksPath .githooks