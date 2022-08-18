from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class TestLoginUser(TestCase, Client):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username='user@gmail.com',
            password='python2022',
            first_name='Вася',
            last_name='Пупкин',
            email='user@mail.com',
            mobile='380650000000',
            slug='user',
        )
        self.user1 = User.objects.create_user(
            username='user1@gmail.com',
            password='python2022',
            first_name='Екатерина',
            last_name='Белова',
            email='user1@mail.com',
            mobile='380650000000',
            slug='user1',
        )
        self.client = Client()

    def test_checking_home_page_elements_page_before_authorization(self):
        response = self.client.get(reverse('gallery:photo-gallery'))
        self.assertTemplateUsed(response, 'photo_gallery/photo-gallery.html')
        self.assertTrue(response.status_code, 200)
        html = response.content.decode('utf-8')

        self.assertInHTML(
            '''<a class="nav-link dropdown-toggle" data-bs-toggle="dropdown"
            href="/user/profile/user/"><i class="fa-solid fa-user"></i>
            user@gmail.com</a>''', html, False
        )

        self.assertInHTML(
            '''<a class="dropdown-item" href="/user/logout/">
            <i class="fa-solid fa-right-from-bracket"></i>
            Logout</a>''', html, False
        )

        self.assertInHTML('''<a class="navbar-brand" href="#">Ironika</a>''', html, True)
        self.assertInHTML('''<a class="nav-link" href="/courses/video/course/">Courses</a>''',
                          html, True)
        self.assertInHTML('''<a class="nav-link" href="/">Gallery</a>''', html, True)

        self.assertInHTML(
            '''<a class="nav-link dropdown-toggle" href="#" id="navbarDropdown"
             role="button" data-bs-toggle="dropdown" aria-expanded="false">Category's</a>''',
            html, True
        )

        self.assertInHTML('''<a class="nav-link" href="/user/login/">Login</a>''',
                          html, True)

        self.assertInHTML('''<a class="nav-link" href="/user/register/">Registration</a>''',
                          html, True)

    def test_login(self):
        response = self.client.get(reverse('user:login'))
        self.assertTemplateUsed(response, 'user/login.html')
        self.client.login(username='user@gmail.com', password='python2022', follow=True)
        response = self.client.get(reverse('gallery:photo-gallery'))
        html = response.content.decode('utf-8')

        self.assertInHTML('''<a class="dropdown-item" href="/user/logout/">
                            <i class="fa-solid fa-right-from-bracket"></i>
                            Logout</a>''', html, True)

        self.assertInHTML('''<a class="dropdown-item" href="/user/profile/user/">
                            <i class="fa-solid fa-address-card"></i> Profile</a>
                            ''', html, True)

        self.assertInHTML('''<a class="nav-link" href="/user/login/">Login</a>''',
                          html, False)

        self.assertInHTML('''<a class="nav-link" href="/user/register/">Registration</a>''',
                          html, False)

    def test_page_user(self):
        self.client.login(username='user@gmail.com', password='python2022', follow=True)
        response = self.client.get(f'/user/profile/user/')
        self.assertTrue(response.status_code, 200)
        html = response.content.decode('utf-8')

        self.assertInHTML('''<title>User page</title>''', html, True)

        self.assertInHTML('''<h5 class="card-title">Welcome Вася Пупкин</h5>''', html, True)

        self.assertInHTML('''<p class="card-text">First Name: Вася</p>''', html, True)

        self.assertInHTML('''<p class="card-text">Last Name: Пупкин</p>''', html, True)

        self.assertInHTML('''<p class="card-text">Telephone: 380650000000</p>''', html, True)

        self.assertInHTML('''<p class="card-text">Email: user@mail.com</p>''', html, True)

    def test_ban_on_viewing_pages_of_other_users(self):
        response = self.client.get('/user/profile/user1/')
        print(response.status_code, '<<<<<')
        self.assertEqual(response.status_code, 302)
        html = response.content.decode('utf-8')
        self.assertInHTML('''<title>User page</title>''', html, False)

        self.assertInHTML('''<h5 class="card-title">Welcome Екатерина Белова</h5>''', html, False)

        self.assertInHTML('''<p class="card-text">First Name: Екатерина</p>''', html, False)

        self.assertInHTML('''<p class="card-text">Last Name: Белова</p>''', html, False)

        self.assertInHTML('''<p class="card-text">Telephone: 380650000000</p>''', html, False)

        self.assertInHTML('''<p class="card-text">Email: user1@mail.com</p>''', html, False)

    def test_ban_on_editing_pages_of_other_users(self):
        response = self.client.get('user/profile/user1/update/')
        self.assertEqual(response.status_code, 404)
