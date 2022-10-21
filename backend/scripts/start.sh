#!/bin/bash

echo "Starting natours server..."
echo "Waiting for postgres..."

while ! nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do
    sleep 0.1
done
echo "PostgreSQL started"

python app/db/init_pg.py

uvicorn app.main:app --host 0.0.0.0 --port 8000
"$@"