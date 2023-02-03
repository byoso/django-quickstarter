#! /bin/bash

# This file will be used with crontab to renew the ssl certificate
# it is not directly related to the application's code

set -e

# use the proper directory names instead of byoso/django_quickstarter
cd /home/byoso/django-quickstarter

docker-compose run --rm certbot sh -c "certbot renew"
