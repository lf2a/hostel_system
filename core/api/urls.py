# django rest framework
from rest_framework import routers

# local django
from core.api.views import SignUpViewSet, LogoutViewSet

router = routers.DefaultRouter()

# /api/signup/
router.register('signup', SignUpViewSet, basename='signup-api')

# /api/logout/
router.register('logout', LogoutViewSet, basename='logout-api')
