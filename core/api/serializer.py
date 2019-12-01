# django rest framework
from rest_framework.serializers import ModelSerializer

# local django
from core.models import Booking
from bedroom.api.serializers import BedroomSerializer


class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        extra_kwargs = {'districts': {'write_only': True}}
        fields = ['id', 'client', 'bedroom', 'total', 'start', 'finish']
