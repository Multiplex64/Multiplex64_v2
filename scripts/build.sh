#!/bin/bash
# Remove development-only files and directories
rm -rf .github/

# Remove markdown files
rm -f README.md
rm -f TODO.md
rm -f DEPLOY.md

# Remove example files
rm -f .env.dev.example
rm -f .env.prod.example
rm -f config/settings/local_settings.py

# Remove scripts
rm -f scripts/check.sh

# Remove this file
rm -f scripts/build.sh