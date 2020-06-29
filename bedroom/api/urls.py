# django rest framework
from rest_framework import routers

# local django
from bedroom.api.views import BedroomViewSet

router = routers.DefaultRouter()

# /bedrooms/api/
router.register('', BedroomViewSet)
