#!/bin/bash
set -e -o pipefail

if [ -n "$MIGRATE" ] && [ "$MIGRATE" = 1 ]; then
    echo "Do database migrations..."
    python ./manage.py migrate 2>&1 > /dev/null
    echo "Initialization complete! Exit."
else
    echo "Run application..."
    python ./manage.py runserver
fi
