#!/bin/bash
# Remove development-only files and directories
rm -rf .github/

# Remove markdown files
rm -f README.md

# Remove example files
rm -f .env.dev.example
rm -f .env.prod.example

# This file's parent folder is deleted by deploy.yml