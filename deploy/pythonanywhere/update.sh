#!/bin/sh
# Run when updating prod server
set -e
git fetch --depth 1
git reset --hard origin/prod
sh scripts/deploy.sh