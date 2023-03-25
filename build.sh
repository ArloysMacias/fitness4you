#!/usr/bin/env bash

set -o errexit  # exit on error

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata products/fixtures/*json
echo "$SU_PASSWORD" | python manage.py createsuperuser --username $SU_USERNAME --email $SU_EMAIL --noinput
