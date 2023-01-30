"""gunicorn WSGI server configuration."""

import os

SSL = os.environ.get('SSL', '0') == '1'
if SSL:
    bind = '0.0.0.0:443'
    keyfile = 'configs/ssl/privkey.pem'
    certfile = 'configs/ssl/cert.pem'
    ca_certs = 'configs/ssl/chain.pem'
else:
    bind = '0.0.0.0:8000'
max_requests = 1000
keepalive = 5
# worker_class = 'gevent'
workers = os.environ.get('GUNICORN_WORKERS', 3)
