#! /usr/bin/env python3
# coding: utf-8

"""Populate the database with some data. Use './manage.py shell < populate.py'
 to run this script in the shell."""


import os
from pathlib import Path

from django.core.files import File
from django.conf import settings

from users.models import User

import dotenv

dotenv.read_dotenv()

POP_DIR = os.path.join(settings.BASE_DIR, "populate_images")
POP_DIR_SH = os.path.abspath(POP_DIR.replace(" ", "\ "))
IMG_DIR = os.path.join(settings.BASE_DIR, "media/images")
IMG_DIR_SH = os.path.abspath(IMG_DIR.replace(" ", "\ "))


def set_images(project, icon_name=None, shot_name=None):
    if icon_name is not None:
        path = Path(os.path.join(IMG_DIR, icon_name))
        with path.open(mode='rb') as f:
            project.icon = File(f, name=path.name)
            project.save()
    if shot_name is not None:
        path = Path(os.path.join(IMG_DIR, shot_name))
        with path.open(mode='rb') as f:
            project.screenshot = File(f, name=path.name)
            project.save()


def create_superuser():
    """Create a superuser."""
    if not User.objects.filter(
            username=os.environ.get('DJANGO_SUPERUSER_USERNAME')).exists():
        user = User.objects.create(
            username=os.environ.get('DJANGO_SUPERUSER_USERNAME'),
            email=os.environ.get('DJANGO_SUPERUSER_EMAIL'),
            is_staff=True,
            is_superuser=True,
        )
        user.set_password(os.environ.get('DJANGO_SUPERUSER_PASSWORD'))
        user.save()
        print("Superuser created!")
    else:
        print("Superuser already exists!")


def populate():
    """Populate the database with some data."""
    create_superuser()
    # add other data here


# in the shell: __name__ == 'django.core.management.commands.shell
print("env POPULATE: ", os.environ.get('POPULATE'))
if str(os.environ.get('POPULATE')) == '1':
    print("Populating script!")
    populate()
    print("Populating done!")
