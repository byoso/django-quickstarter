#! /bin/bash


SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"default@admin.com"}
cd /web

# this is ugly but we need to wait for the database to be ready
# if in another container (temporary, should do that another way):
sleep 5s

./manage.py migrate --noinput
./manage.py collectstatic --noinput

# populate the database with some data
# the superuser can be created here
./manage.py shell < populate.py

echo "MIGRATE.SH EXECUTED"