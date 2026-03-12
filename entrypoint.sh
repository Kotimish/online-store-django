#!/usr/bin/env bash

set -e

echo "Applying migrations..."
python manage.py migrate
echo "Done migrations, starting app..."

exec "$@"