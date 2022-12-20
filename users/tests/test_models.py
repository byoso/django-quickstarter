#! /usr/bin/env python3
# coding: utf-8

from users.models import User
from django.test import TestCase, Client


class TestModels(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(
            username='testuser', email='test@test.com')
        self.user.set_password('testpass1')
        self.user.save()

    def test_jwt_token(self):
        user = User.objects.get(username='testuser')
        self.client.login(username='testuser', password='testpass1')
        token = user.get_jwt_token()
        jwt_user = User.verify_token(token)
        self.assertEqual(jwt_user, user)
