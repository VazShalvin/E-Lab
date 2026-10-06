#!/bin/bash
set -e

# Wait for database to be ready
until python manage.py check --database default; do
  echo "Waiting for database..."
  sleep 2
done

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate --noinput

# Run semester auto-advance (only acts on Jan 1 and Jul 1)
echo "Checking semester transitions..."
python manage.py auto_advance_semesters

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

if [ $# -eq 0 ]; then
    echo "Starting Gunicorn with production settings..."
    exec gunicorn config.wsgi:application \
        --bind 0.0.0.0:8000 \
        --workers 12 \
        --threads 4 \
        --worker-class gthread \
        --max-requests 1000 \
        --max-requests-jitter 100 \
        --timeout 60 \
        --keep-alive 5 \
        --log-level info \
        --access-logfile - \
        --error-logfile - \
        --preload
else
    echo "Running command: $@"
    exec "$@"
fi