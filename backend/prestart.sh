#!/bin/sh

# Add environment variables from .env file
# export $(egrep -v '^#' .env | xargs)

# Install packages for development
# pip install -U pip
# pip install -r requirements.txt

# Create superuser
# python manage.py createsuperuser \
#    --noinput \
#    --username $DJANGO_SUPERUSER_USERNAME \
#    --email $DJANGO_SUPERUSER_EMAIL

# Migrations
# python manage.py migrate
