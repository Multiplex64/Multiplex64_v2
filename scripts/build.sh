#!/bin/bash
# Remove development-only files and directories

# Remove Github folder
rm -rf .github/

# Remove markdown files
rm -f README.md
rm -f TODO.md
rm -f DEPLOY.md

# Remove example files
rm -f .env.dev.example
rm -f .env.prod.example

# Remove hooks
rm -f .githooks/pre-push

# Remove this file
rm -f scripts/build.sh