#! /bin/bash


SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"default@admin.com"}
cd /web

# this is ugly but we need to wait for the database to be ready
# if in another container (temporary, should do that another way):
sleep 5s

./manage.py migrate --noinput
./manage.py collectstatic --noinput

# Superuser: create him here or within the populate.py script
# django automatically checks the environment variables
# DJANGO_SUPERUSER_USERNAME and DJANGO_SUPERUSER_PASSWORD
# to create the superuser with all the parameters
./manage.py createsuperuser --email $SUPERUSER_EMAIL --noinput || true

# populate the database with some data
./manage.py shell < populate.py

echo "MIGRATE.SH EXECUTED"