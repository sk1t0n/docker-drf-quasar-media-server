#!/bin/sh

# Add environment variables from .env file
# export $(egrep -v '^#' .env | xargs)

# Install packages for development
# pip install -U pip
# pip install -r requirements.txt

# Migrations
# python manage.py makemigrations
# python manage.py migrate

# Create superuser
# python manage.py createsuperuser \
#    --noinput \
#    --username $DJANGO_SUPERUSER_USERNAME \
#    --email $DJANGO_SUPERUSER_EMAIL
