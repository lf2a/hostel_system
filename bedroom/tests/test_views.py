# django
from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy

# local django
from bedroom.models import Bedroom


class BedroomListTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_bedroom_list_view(self):
        request = self.client.get(reverse_lazy('bedrooms'))
        self.assertEquals(request.status_code, 200)


class BedroomDetailView(TestCase):

    def setUp(self):
        self.client = Client()
        bedroom = Bedroom(id=1, number=1, floor=1, bathroom=1, bed=1, daily=120.8)
        bedroom.save()

    def test_bedroom_detail_view(self):
        request = self.client.get(reverse_lazy('bedroom', kwargs={'pk': 1}))
        self.assertEquals(request.status_code, 200)
