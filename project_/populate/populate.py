#! /usr/bin/env python3
# coding: utf-8

"""Populate the database with some data. Use './manage.py shell < populate.py'
 to run this script in the shell."""


import os
from pathlib import Path

from django.core.files import File
from django.conf import settings


POP_DIR = os.path.join(settings.BASE_DIR, "populate_images")
POP_DIR_SH = os.path.abspath(POP_DIR.replace(" ", "\ "))
IMG_DIR = os.path.join(settings.BASE_DIR, "media/images")
IMG_DIR_SH = os.path.abspath(IMG_DIR.replace(" ", "\ "))

# may be used in some project, otherwise just delete it
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


def populate():
    """Populate the database with some data."""
    print("Populating...")

    # add some data here

    print("Populating done!")
