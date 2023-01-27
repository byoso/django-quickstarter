#! /bin/bash


cd /web/configs
chmod +x migrate.sh
./migrate.sh
cd /web
gunicorn --bind 0.0.0.0:8000 -w 3 project_.wsgi:application


echo "ENTRYPOINT.SH EXECUTED"