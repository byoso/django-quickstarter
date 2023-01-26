# Django Quickstarter

*Boilerplate for django 4.x*

The goal here is to provide a django starter kit with a complete authentication system, and canvas for docker / docker-compose ready for
deployment.

## First

Rename 'project_' into something more apropriate, then search and change
 the word 'project_' in a few files:
- manage.py
- settings.py
- prod_config/entrypoint.sh (the gunicorn command)

Use `dependencies_pip.txt` to create the environment, and then pip freeze it
to `requirements.txt`.

## Environment variables

Environment variables are stored in the `.env` file, override them on the
server in production.

### General settings

When switching from dev to prod, this are the settings you want to change
 in `.env`:
```
# simple django debug option
DEBUG=1
# if DB is not postges, it will be sqlite by default
DB_IS_POSTGRESQL=0
# set 1: when you have properly configured an email to be
# used by your web site like a "no-replay@my_site.com"
# set 0: the emails sent will be emulated in console
EMAIL_IS_CONFIGURED=0
```
The other settings are quite self-explainatory.

## Tests

`coverage run ./manage.py test -v 2` # [-v 2 ] is for verbose

`coverage report` to see the report
