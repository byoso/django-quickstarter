from django.test import TestCase, Client
from django.urls import reverse


from users.models import User


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(
            username='testuser', email='test@test.com')
        self.user.set_password('testpass1')
        self.user.save()

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_login_view_GET(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

    def test_login_view_POST(self):
        logged_in = self.client.login(username="Unknown", password="wrong")
        self.assertEqual(logged_in, False)
        logged_in = self.client.login(
            username="testuser", password="testpass1")
        self.assertEqual(logged_in, True)

        response = self.client.post(
            reverse("login"),
            {"username": 'testuser', 'password': 'testpass1'})
        self.assertEqual(response.status_code, 200)
        user = User.objects.get(username='testuser')
        self.assertEqual(user.is_authenticated, True)

    def test_signin_GET(self):
        response = self.client.get(reverse('signin'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/signin.html")

    def test_signin_POST(self):
        response = self.client.post(reverse('signin'), {
            'username': 'new_user',
            'email': 'new_mail@mail.com'
        })

        user = User.objects.get(username="new_user")
        user.save()
        self.assertEqual(response.status_code, 302)
        user = User.objects.filter(username="new_user")
        self.assertEqual(len(user), 1)
        user2 = User.objects.filter(username="no_user")
        self.assertEqual(len(user2), 0)

    def test_account_view(self):
        self.client.login(username='testuser', password='testpass1')
        response = self.client.get(reverse('account'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/account.html')
        self.assertContains(response, 'testuser')

    def test_request_password_reset_GET(self):
        response = self.client.get(reverse('request_password_reset'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/request_password_reset.html')

    def test_request_password_reset_POST(self):
        response = self.client.post(reverse('request_password_reset'), {
            'email': 'some@mail.com'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/request_password_reset.html')

    def test_change_username_GET(self):
        self.client.login(username='testuser', password='testpass1')
        response = self.client.get(reverse('change_username'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/change_username.html')

    def test_change_username_POST(self):
        self.client.login(username='testuser', password='testpass1')
        response = self.client.post(reverse('change_username'), {
            'username': 'new_username'
        })
        self.assertEqual(response.status_code, 302)
        user = User.objects.get(username='new_username')
        self.assertEqual(user.username, 'new_username')

    def test_change_email_GET(self):
        self.client.login(username='testuser', password='testpass1')
        response = self.client.get(reverse('change_email'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/change_email.html')

    def test_change_email_POST(self):
        self.client.login(username='testuser', password='testpass1')
        user = User.objects.get(username='testuser')
        self.assertIsNone(user.unconfirmed_email)
        response = self.client.post(reverse('change_email'), {
            'email': 'new@test.com'})
        self.assertEqual(response.status_code, 200)
        user = User.objects.get(username='testuser')
        self.assertIsNotNone(user.unconfirmed_email)
