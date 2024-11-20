#!/bin/bash
set -e -o pipefail

# ./wait-for.sh rabbit:5672 -t 15

if [ -n "$MIGRATE" ] && [ "$MIGRATE" = 1 ]; then
    echo "Do database migrations..."
    echo "Initialization complete! Exit."
else
    celery -A application worker --loglevel=INFO
fi