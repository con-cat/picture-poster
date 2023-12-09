#! /bin/bash
set -e

cd /app/src

./manage.py migrate --noinput
./manage.py setup_local_dev_user
./manage.py runserver 0.0.0.0:8000
