# django
from django.urls import path

# local django
from bedroom.views import BedroomList, BedroomDetailView

urlpatterns = [
    # /bedroom/
    path('', BedroomList.as_view(), name='bedrooms'),

    # /bedroom/<int:pk>/
    path('<int:pk>/', BedroomDetailView.as_view(), name='bedroom')
]
