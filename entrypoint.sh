#!/bin/bash

cd /app
# DB migrate
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput

# 초기 superuser 계정 생성
echo "Create admin user"
CREATE_ADMIN_SOURCE="
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
UserModel = get_user_model()
# Create admin user
USERNAME='pyconkr'
EMAIL='pyconkr@pycon.kr'
# Should be changed
PASSWORD='pyconkr'
try:
    UserModel.objects.get(username=USERNAME)
except UserModel.DoesNotExist:
    User.objects.create_superuser(USERNAME, EMAIL, PASSWORD)
"
echo "${CREATE_ADMIN_SOURCE}"  | python manage.py shell

# RUN
gunicorn -b 0.0.0.0:8000 pyconkr.wsgi:application
