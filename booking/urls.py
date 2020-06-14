# django
from django.urls import path

# local django
from booking.views import BookingListView, BookingCreateView, BookingDeleteView

urlpatterns = [
    # /booking/
    path('', BookingListView.as_view(), name='bookings'),

    # /booking/<str:id>/book
    path('<str:id>/book/', BookingCreateView.as_view(), name='booking_new'),

    # /booking/<str:id>/delete/
    path('<str:id>/delete', BookingDeleteView.as_view(), name='booking_delete'),
]
