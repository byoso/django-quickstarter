
from django.test import TestCase

from users.models import User
from users.forms import (
    SignInForm,
    LoginForm,
    RequestPasswordResetForm,
    ResetPasswordForm,
    ChangeUsernameForm,
    ChangeEmailForm,
    )


class TestForms(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='testuser', email='test@test.com')
        self.user.set_password('testpass1')
        self.user.save()

    def test_login_form(self):
        form = LoginForm(data={
            'login': 'testuser',
            'password': 'testpass1'
        })
        self.assertTrue(form.is_valid())
        form = LoginForm(data={
            'login': '',
            'password': ''
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)

    def test_sign_in_form(self):
        form = SignInForm(data={
            'username': 'testuser2',
            'email': 'test2@test.com'
        })
        self.assertTrue(form.is_valid())
        form = SignInForm(data={
            'username': '',
            'email': ''
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)

    def test_request_password_reset_form(self):
        form = RequestPasswordResetForm(data={
            'email': 'test@test.com'
        })
        self.assertTrue(form.is_valid())
        form = RequestPasswordResetForm(data={
            'email': 'unknown@mail.com'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    def test_reset_password_form(self):
        form = ResetPasswordForm(data={
            'password': 'testpass2',
            'password2': 'testpass2'
        })
        self.assertTrue(form.is_valid())
        form = ResetPasswordForm(data={
            'password': 'testpass2',
            'password2': 'other'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    def test_change_username_form(self):
        form = ChangeUsernameForm(data={
            'username': 'new_username'
        })
        self.assertTrue(form.is_valid())
        form = ChangeUsernameForm(data={
            'username': ''
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    def test_change_email_form(self):
        form = ChangeEmailForm(data={
            'email': 'new@email.com'
        })
        self.assertTrue(form.is_valid())
        form = ChangeEmailForm(data={
            'email': 'test@test.com'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)
