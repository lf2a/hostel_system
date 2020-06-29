# django
from django.urls import path, include

# local django
from bedroom.views import BedroomList, BedroomDetailView
from bedroom.api.urls import router

urlpatterns = [
    # /bedroom/
    path('', BedroomList.as_view(), name='bedrooms'),

    # /bedroom/<int:pk>/
    path('<int:pk>/', BedroomDetailView.as_view(), name='bedroom'),

    # /bedroom/api/
    path('api/', include(router.urls))
]
