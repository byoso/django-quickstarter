from django.test import TestCase
from django.urls import reverse, resolve
from users.views import (
    index,
    login_view,
    logout_view,
    signin_view,
    account,
    request_password_reset,
    reset_password,
    change_username,
    change_email,
    confirm_email,
)


class TestSimple(TestCase):
    def test_index_url(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)

    def test_login_url(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, login_view)

    def test_signin_url(self):
        url = reverse('signin')
        self.assertEqual(resolve(url).func, signin_view)

    def test_logout_url(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, logout_view)

    def test_account_url(self):
        url = reverse('account')
        self.assertEqual(resolve(url).func, account)

    def test_request_password_reset_url(self):
        url = reverse('request_password_reset')
        self.assertEqual(resolve(url).func, request_password_reset)

    def test_reset_password_url(self):
        url = reverse('reset_password', args=['token'])
        self.assertEqual(resolve(url).func, reset_password)

    def test_change_username_url(self):
        url = reverse('change_username')
        self.assertEqual(resolve(url).func, change_username)

    def test_change_email_url(self):
        url = reverse('change_email')
        self.assertEqual(resolve(url).func, change_email)

    def test_confirm_email_url(self):
        url = reverse('confirm_email', args=['token'])
        self.assertEqual(resolve(url).func, confirm_email)