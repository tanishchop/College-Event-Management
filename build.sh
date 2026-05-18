#!/usr/bin/env bash
# build.sh — Render runs this on every deploy

set -o errexit   # Exit immediately on any error

# 1. Install Python dependencies
pip install -r requirements.txt

# 2. Apply database migrations
python manage.py migrate --no-input

# 3. Collect static files into STATIC_ROOT for WhiteNoise to serve
python manage.py collectstatic --no-input
