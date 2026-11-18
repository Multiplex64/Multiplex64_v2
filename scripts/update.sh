#!/bin/sh
# Run when updating dev environment
set -e
git pull origin main
./scripts/deploy.sh