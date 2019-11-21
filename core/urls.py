# django
from django.urls import path

# local django
from .views import bookings, booking_create, BookingUpdate, BookingDelete

urlpatterns = [
    # /booking/
    path('', bookings, name='bookings'),

    # /booking/delete/<str:id>/
    path('delete/<str:id>', BookingDelete.as_view(), name='booking_delete'),

    # /booking/create/
    path('create/', booking_create, name='booking_create'),

    # /booking/update/<str:id>/
    path('update/<str:id>', BookingUpdate.as_view(), name='booking_update'),
]
