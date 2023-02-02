#! /bin/sh

# Wait for proxy to be available then get the first certificate

set -e

until nc -z nginx 80; do
    echo "Waiting for nginx to be available"
    sleep 2s
done

echo "Nginx is available, getting certificate"

certbot certonly \
    --webroot \
    --webroot-path "/vol/www/" \
    --rsa-key-size 4096 \
    --non-interactive \
    --agree-tos \
    --email "$ACME_DEFAULT_EMAIL" \
    -d "$DOMAIN"
