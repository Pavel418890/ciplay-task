#!/usr/bin/env bash

set -e
set -x

echo "Starting natours server..."
echo "Waiting for postgres..."

while ! nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do
    sleep 0.1
done
echo "PostgreSQL started"
pwd
ls -la

python /usr/src/ciplay-task/app/db/init_pg.py ${@}

