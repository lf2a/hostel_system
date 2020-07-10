# django
from django.test import TestCase

# local django
from core.forms import ContactForm


class ContactFormTestCase(TestCase):

    def setUp(self):
        self.name = 'Luiz Filipy'
        self.email = 'luizfilipy014@gmail.com'
        self.message = 'Uma mensagem qualquer'

        self.data = {
            'name': self.name,
            'email': self.email,
            'message': self.message
        }

        self.form = ContactForm(data=self.data)

    def test_send_mail(self):
        form1 = ContactForm(data=self.data)
        form1.is_valid()
        res1 = form1.send_mail()

        form2 = self.form
        form2.is_valid()
        res2 = form2.send_mail()

        self.assertEquals(res1, res2)
