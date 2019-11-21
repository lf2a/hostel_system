# django
from django.urls import path

# local django
from .views import bedrooms, bedroom

urlpatterns = [
    # /bedroom/
    path('', bedrooms, name='bedrooms'),

    # /bedroom/<str:id>/
    path('<str:id>/', bedroom, name='bedroom')
]
