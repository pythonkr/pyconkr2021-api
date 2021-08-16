#!/bin/bash

cd /app
# DB migrate
python manage.py makemigrations
python manage.py migrate

# RUN
gunicorn -b 0.0.0.0:8000 pyconkr.asgi:application
