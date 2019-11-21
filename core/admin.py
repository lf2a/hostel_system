# django
from django.contrib import admin

# local django
from .models import Booking

# registra o model
admin.site.register(Booking)