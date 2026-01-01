#!/usr/bin/env bash
set -o errexit

echo "Running migrations..."

python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting Gunicorn..."
gunicorn ecommerce.wsgi:application
