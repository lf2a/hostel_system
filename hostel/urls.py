# django
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # hostel system core
    path('', include('core.urls')),

    # bedroom
    path('bedroom/', include('bedroom.urls')),

    # user
    path('my/', include('client.urls')),

    # booking
    path('booking/', include('booking.urls')),

    # admin area
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
