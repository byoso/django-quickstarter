#! /bin/sh


cd /web

# this is ugly but we need to wait for the database to be ready
# if in another container (temporary, should do that another way):
sleep 5s

python manage.py migrate --noinput
python manage.py collectstatic --noinput

if [ "$CREATE_SUPERUSER" = "1" ]; then
    python manage.py shell < configs/populate/createsuperuser.py
fi

if [ "$POPULATE" = "1" ]; then
    python manage.py shell < configs/populate/populate.py
fi


echo "MIGRATE.SH EXECUTED"