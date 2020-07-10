from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy


class HomePageViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_home_page(self):
        request = self.client.get(reverse_lazy('index'))
        self.assertEquals(request.status_code, 200)


class ContactViewTestCase(TestCase):
    def setUp(self):
        self.data = {
            'name': 'Luiz Filipy',
            'email': 'luizfilipy014@gmail.com',
            'message': 'Minha mensagem'
        }
        self.client = Client()

    def test_form_valid(self):
        request = self.client.post(reverse_lazy('send_email'), data=self.data)
        self.assertEquals(request.status_code, 302)

    def test_form_invalid(self):
        data = {
            'name': 'Luiz Filipy'
            # without email and message field
        }
        request = self.client.post(reverse_lazy('send_email'), data=data)
        self.assertEquals(request.status_code, 200)

    def test_invalid_http_method(self):
        request = self.client.get(reverse_lazy('send_email'))
        self.assertEquals(request.status_code, 302)


class LogoutViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_logout(self):
        request = self.client.get(reverse_lazy('logout'))
        self.assertEquals(request.status_code, 302)


class SignUpViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_valid_signup(self):
        data = {
            'email': 'luizfilipy.aa@outlook.com',
            'username': 'lfaa',
            'password1': 'almeida1367',
            'password2': 'almeida1367'
        }
        request = self.client.post(reverse_lazy('signup'), data=data)
        self.assertEquals(request.status_code, 302)

    def test_invalid_signup(self):
        data = {
            'email': 'luizfilipy.aa@outlook.com',
            'username': 'lfaa'
        }
        request = self.client.post(reverse_lazy('signup'), data=data)
        self.assertEquals(request.status_code, 200)
