# django
from django.test import TestCase

# local django
from bedroom.models import Bedroom, BedroomImage


class BedroomTestCase(TestCase):

    def setUp(self):
        self.bedroom = Bedroom(id=1, number=2, floor=1, bathroom=1, bed=1, daily=120.8)
        self.bedroom_image = BedroomImage(bedroom=self.bedroom)

    def test_bedroom(self):
        self.assertEquals(str(self.bedroom), 'F1 - N2')

    def test_bedroom_image(self):
        self.assertEquals(str(self.bedroom_image), 'F1 - N2')
