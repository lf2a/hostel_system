# django
from django.urls import path, include

# local django
from booking.views import BookingListView, BookingCreateView, BookingDeleteView
from booking.api.urls import router

urlpatterns = [
    # /booking/
    path('', BookingListView.as_view(), name='bookings'),

    # /booking/<str:id>/book
    path('<str:id>/book/', BookingCreateView.as_view(), name='booking_new'),

    # /booking/<str:id>/delete/
    path('<str:id>/delete', BookingDeleteView.as_view(), name='booking_delete'),

    # /booking/api/
    path('api/', include(router.urls)),
]
