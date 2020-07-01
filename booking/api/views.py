# python
from datetime import datetime

# django
from django.shortcuts import get_object_or_404

# django rest framework
from rest_framework import viewsets
from rest_framework import response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# local django
from booking.api.serializers import BookingSerializer
from booking.models import Booking
from bedroom.models import Bedroom


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset.filter(client_id=user.id)
        return queryset

    def retrieve(self, request, *args, **kwargs):
        booking_id = kwargs.get('pk')
        booking = get_object_or_404(Booking, id=booking_id)
        if request.user.id == booking.client.id:
            booking_serializer = BookingSerializer(booking)
            return response.Response(data=booking_serializer.data, status=200)
        return response.Response(status=404)

    def create(self, request, *args, **kwargs):
        bedroom_id = self.request.data['bedroom']
        bedroom = get_object_or_404(Bedroom, id=bedroom_id)

        if bedroom.is_available:
            start_booking = datetime.strptime(self.request.data['start'], '%Y-%m-%d').date()
            finish_booking = datetime.strptime(self.request.data['finish'], '%Y-%m-%d').date()
            user = self.request.user
            new_booking = Booking(client=user, bedroom=bedroom, start=start_booking, finish=finish_booking)
            bedroom.is_available = False
            new_booking.save()
            bedroom.save()
            new_booking_serializer = BookingSerializer(new_booking)
            return response.Response(data=new_booking_serializer.data, status=201)
        return response.Response(data='This room has already been booked or does not exist', status=400)

    def update(self, request, *args, **kwargs):
        return response.Response(status=405)

    def partial_update(self, request, *args, **kwargs):
        return response.Response(status=405)

    def destroy(self, request, *args, **kwargs):
        booking = get_object_or_404(Booking, id=kwargs.get('pk'))

        if request.user.id == booking.client.id:
            bedroom = Bedroom.objects.get(id=booking.bedroom.id)
            bedroom.is_available = True
            booking.delete()
            bedroom.save()
            return response.Response(status=200)
        return response.Response(status=404)
