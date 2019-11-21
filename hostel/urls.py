# django
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500

# local django
from .views import index, about, logout_system, SignUp, error_404_view

urlpatterns = [
    # hostel
    path('', index, name='index'),
    path('about/', about, name='about'),

    # bedroom
    path('bedroom/', include('bedroom.urls')),

    # user
    path('user/', include('client.urls')),
    
    # booking
    path('booking/', include('core.urls')),


    # authentication
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('logout/', logout_system, name='logout'),

    # admin area
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

handler404 = 'hostel.views.error_404_view'
handler500 = 'hostel.views.error_500_view'