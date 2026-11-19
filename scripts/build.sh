#!/bin/sh
# Remove development-only files and directories

# Remove Github folder
rm -rf .github/

# Remove markdown files
rm -f README.md
rm -f DEPLOY.md

# Remove example files
rm -f .env.dev.example
rm -f .env.prod.example

# Remove dev hooks
rm -f .githooks/

# Remove scripts
rm -f scripts/setup.sh
rm -f scripts/update.sh
rm -f scripts/test-dev.sh

# Move pythonanywhere scripts
cp deploy/pythonanywhere/update.sh scripts/update.sh

# Remove deploy
rm -rf deploy/

# Remove this file
rm -- "$0"