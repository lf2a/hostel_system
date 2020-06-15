# django
from django.urls import path
from django.contrib.auth import views as auth_views

# local django
from core.views import HomePageView, ContactView, SignUpView, LogoutView

urlpatterns = [
    # /
    path('', HomePageView.as_view(), name='index'),

    # only POST
    # /send-email/
    path('send-email/', ContactView.as_view(), name='send_email'),

    # /login/
    path('login/', auth_views.LoginView.as_view(), name='login'),

    # /signup/
    path('signup/', SignUpView.as_view(), name='signup'),

    # /logout/
    path('logout/', LogoutView.as_view(), name='logout'),
]
