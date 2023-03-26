#!/usr/bin/env bash

set -o errexit  # exit on error

pip install -r requirements.txt
python manage.py collectstatic
python manage.py migrate
echo "$SU_PASSWORD" | python manage.py createsuperuser --username $SU_USERNAME --email $SU_EMAIL --noinput || true
python manage.py loaddata products/fixtures/*json
