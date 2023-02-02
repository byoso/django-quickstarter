#! /bin/sh

set -e

cd /web/configs
chmod +x migrate.sh
./migrate.sh
cd /web


uwsgi --socket :8000 --workers ${WORKERS} --master --enable-threads --module project_.wsgi


echo "ENTRYPOINT.SH EXECUTED"