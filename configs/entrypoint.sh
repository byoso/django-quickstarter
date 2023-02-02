#! /bin/sh

set -e

cd /web/configs
chmod +x migrate.sh
./migrate.sh
cd /web

if [ "$DEBUG" == "1" ]; then
    echo "DEBUG is 1, starting gunicorn"
    gunicorn --bind :8000 -w ${WORKERS} project_.wsgi
else
    echo "DEBUG is 0, starting uwsgi"
    uwsgi --socket :8000 --workers ${WORKERS} --master --enable-threads --module project_.wsgi
fi



echo "ENTRYPOINT.SH EXECUTED"