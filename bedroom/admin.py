# django
from django.contrib import admin

# django local
from .models import Bedroom, BedroomImage

admin.site.register(Bedroom)
admin.site.register(BedroomImage)
