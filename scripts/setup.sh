#!/bin/sh
# Run when cloning and initializing repository in dev
./scripts/deploy.sh
git config core.hooksPath .githooks