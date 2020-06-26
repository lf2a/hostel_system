# django
from django.urls import path

# local django
from client.views import UserProfileTemplateView, UserUpdateView, UserDeleteView
from client.api.views import UserView

urlpatterns = [
    # /my/profile/
    path('profile/', UserProfileTemplateView.as_view(), name='user_detail'),

    # /my/update/
    path('update/', UserUpdateView.as_view(), name='update_info'),

    # /my/delete/
    path('delete/', UserDeleteView.as_view(), name='delete_account'),

    # /my/api/
    path('api/', UserView.as_view(), name='user_api')
]
