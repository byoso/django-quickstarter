#! /bin/bash


cd /web

# this is ugly but we need to wait for the database to be ready
# if in another container (temporary, should do that another way):
sleep 5s

./manage.py migrate --noinput
./manage.py collectstatic --noinput

./manage.py shell < configs/populate/createsuperuser.py
./manage.py shell < configs/populate/populate.py

echo "MIGRATE.SH EXECUTED"