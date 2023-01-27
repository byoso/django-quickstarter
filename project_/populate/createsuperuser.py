#! /usr/bin/env python3
# coding: utf-8

import os

from users.models import User


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