# django rest framework
from rest_framework import serializers

# local django
from bedroom.models import Bedroom, BedroomImage


class BedroomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BedroomImage
        fields = ['url']


class BedroomSerializer(serializers.ModelSerializer):
    photos = BedroomImageSerializer(many=True, read_only=True)

    class Meta:
        model = Bedroom
        fields = ['number', 'floor', 'bathroom', 'bed', 'daily', 'photos']
