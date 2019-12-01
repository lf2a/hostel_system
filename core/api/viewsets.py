# django rest framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND

# local django
from core.models import Booking
from .serializer import BookingSerializer


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def list(self, request, *args, **kwrags):
        self.queryset = Booking.objects.filter(client__id=request.user.id)
        res = BookingSerializer(self.queryset, many=True)
        return Response(res.data)

    def retrieve(self, request, *args, **kwargs):
        data = {
            'error': {
                'code': 404,
                'message': 'Not Found'
            }
        }
        return Response(data=data, status=HTTP_404_NOT_FOUND)

    def partial(self, request, *args, **kwargs):
        data = {
            'error': {
                'code': 404,
                'message': 'Not Found'
            }
        }
        return Response(data=data, status=HTTP_404_NOT_FOUND)

    def partial_update(self, request, *args, **kwargs):
        data = {
            'error': {
                'code': 404,
                'message': 'Not Found'
            }
        }
        return Response(data=data, status=HTTP_404_NOT_FOUND)

    def destroy(self, request, *args, **kwargs):
        data = {
            'error': {
                'code': 404,
                'message': 'Not Found'
            }
        }
        return Response(data=data, status=HTTP_404_NOT_FOUND)
