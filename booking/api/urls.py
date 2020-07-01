# django rest framework
from rest_framework import routers

# local django
from booking.api.views import BookingViewSet

router = routers.DefaultRouter()

# /booking/api/
router.register('', BookingViewSet)
