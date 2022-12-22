# Django Quickstarter

*Boiletplate for django applications*

The goal here is to provide a django starter application with a complete
authentication system, and canvas for docker / docker-compose ready for
deployment.

## First

Rename 'project_' into something more apropriate, then change the word 'project_' in a few files:
- manage.py
- settings.py
- Dockerfile (the gunicorn command)


## Environment variables

### Production

Do not forget to set this on the server :

- SECRET_KEY
- EMAIL_HOST_PASSWORD

Some other variables are set in docker-compose.yml, check it to configure the application.
