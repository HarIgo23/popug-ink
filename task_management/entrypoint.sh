#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

if [ "$FLUSH_DB" = "1" ]
then
    python manage.py flush --no-input
fi
python manage.py migrate

exec "$@"