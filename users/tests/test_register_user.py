from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.test import TestCase, Client
from django.urls import reverse


class TestRegisterUser(TestCase, Client):

    def setUp(self):
        self.client = Client()
        Group.objects.create(name='groups_user')

    def test_registration_check(self):
        User = get_user_model()
        User.objects.all().delete()

        urls = self.client.get(reverse('user:register'))
        self.assertTemplateUsed(urls, 'user/register_user.html')
        self.assertTrue(urls.status_code, 200)
        self.assertEqual(User.objects.count(), 0)

        self.client.post(reverse('user:register'), {
            'username': 'user@gmail.com',
            'password1': 'python2022',
            'password2': 'python2022',
            'mobile': '380950000000',
            'first_name': 'Вася',
            'last_name': 'Пупкин',
        })
        self.assertEqual(User.objects.count(), 1)

        self.user = User.objects.get(pk=1)
        self.assertEqual(self.user.username, 'user@gmail.com')
        self.assertEqual(self.user.email, 'user@gmail.com')
        self.assertEqual(self.user.slug, 'user')
        response = self.client.get(f'/user/profile/{self.user.slug}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/user_page.html')
