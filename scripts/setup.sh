#!/bin/sh
# Run when cloning and initializing repository
sh scripts/deploy.sh
git config core.hooksPath .githooks