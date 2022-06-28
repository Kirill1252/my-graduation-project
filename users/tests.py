from django.contrib.auth.models import Group
from django.test import TestCase, Client
from django.urls import reverse

from .models import CustomUser


class CustomUserModelTesting(TestCase):

    def setUp(self):
        CustomUser.objects.all().delete()

    def test_adding_a_user_to_the_model(self):
        self.assertEqual(CustomUser.objects.count(), 0)
        self.user1 = CustomUser.objects.create_user(username='User1',
                                                    slug='User1',
                                                    password='python2022',
                                                    mobile='123456789123',
                                                    email='user1@gmail.com'
                                                    )
        self.user2 = CustomUser.objects.create_user(username='User2',
                                                    slug='User2',
                                                    password='python2022',
                                                    mobile='380335478944',
                                                    email='user2@gmail.com'
                                                    )
        self.assertEqual(CustomUser.objects.count(), 2)
        self.assertEqual(self.user1.username, 'User1')
        self.assertEqual(self.user1.mobile, '123456789123')
        self.assertEqual(self.user1.email, 'user1@gmail.com')
        self.assertEqual(self.user1.slug, 'User1')

        self.assertEqual(self.user2.username, 'User2')
        self.assertEqual(self.user2.mobile, '380335478944')
        self.assertEqual(self.user2.email, 'user2@gmail.com')
        self.assertEqual(self.user2.slug, 'User2')


class RegisterUserFormTesting(TestCase):

    def setUp(self):
        CustomUser.objects.all().delete()
        self.c = Client()

    def test_user_registration_via_form(self):
        self.assertEqual(CustomUser.objects.count(), 0)
        response = self.c.get(reverse('user:register'))
        self.assertEqual(200, response.status_code)
        self.c.post(reverse('user:register'), {
            'username': 'user1',
            'password1': 'python2022',
            'password2': 'python2022',
            'mobile': '123564897532',
            'email': 'user1@mail.com',
            'avatar': 'user/test_img/img_user1.jpg'
        })
        self.assertEqual(CustomUser.objects.count(), 1)
        # group = Group.objects.create(name='groups_user')
        # self.user[0].groups.add(group)
        self.user = CustomUser.objects.all()
        self.assertEqual(self.user[0].username, 'user1')
        self.assertEqual(self.user[0].slug, 'user1')
        self.assertEqual(self.user[0].email, 'user1@mail.com')
