# django rest framework
from rest_framework import serializers

# local django
from booking.models import Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'client', 'bedroom', 'total', 'start', 'finish']
