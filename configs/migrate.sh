#! /bin/sh


cd /web

# this is ugly but we need to wait for the database to be ready
# if in another container (temporary, should do that another way):
sleep 5s

python manage.py migrate --noinput
python manage.py collectstatic --noinput

python manage.py shell < configs/populate/createsuperuser.py
python manage.py shell < configs/populate/populate.py

echo "MIGRATE.SH EXECUTED"