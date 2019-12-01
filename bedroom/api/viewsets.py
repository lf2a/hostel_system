# django rest framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_405_METHOD_NOT_ALLOWED

# local django
from bedroom.models import Bedroom, BedroomImage
from core.models import Booking
from .serializers import BedroomSerializer


class BedroomViewSet(ModelViewSet):
    queryset = Bedroom.objects.all()
    serializer_class = BedroomSerializer
    
    def list(self, request, *args, **kwargs):
        bedroom = Bedroom.objects.all()
        booking = Booking.objects.all()

        available_rooms = []
        for b in booking:
            available_rooms.append(b.bedroom)

        queryset = set(bedroom).difference(set(available_rooms))
        
        res = BedroomSerializer(queryset, many=True)
        return Response(res.data)

    def create(self, request, *args, **kwargs):
        data = {
            'error': {
                'code': 405,
                'message': 'Method Not Allowed'
            }
        }
        return Response(data=data, status=HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        data = {
            'error': {
                'code': 405,
                'message': 'Method Not Allowed'
            }
        }
        return Response(data=data, status=HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        data = {
            'error': {
                'code': 405,
                'message': 'Method Not Allowed'
            }
        }
        return Response(data=data, status=HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        data = {
            'error': {
                'code': 405,
                'message': 'Method Not Allowed'
            }
        }
        return Response(data=data, status=HTTP_405_METHOD_NOT_ALLOWED)
