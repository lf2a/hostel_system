# django rest framework
from rest_framework.serializers import ModelSerializer, HyperlinkedRelatedField

# local django
from bedroom.models import Bedroom, BedroomImage

'''
https://www.django-rest-framework.org/api-guide/relations/#nested-relationships
'''


class BedroomImageSerializer(ModelSerializer):
    class Meta:
        model = BedroomImage
        fields = ['id', 'url']


class BedroomSerializer(ModelSerializer):
    photos = BedroomImageSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Bedroom
        fields = [
            'id',
            'number',
            'floor',
            'bathroom',
            'bed',
            'daily',
            'photos'
        ]
