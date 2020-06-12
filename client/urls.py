# django
from django.urls import path

# local django
from client.views import UserProfileTemplateView, UserUpdateView, UserDeleteView

urlpatterns = [
    # /my/profile/
    path('profile/', UserProfileTemplateView.as_view(), name='user_detail'),

    # /my/update/
    path('update/', UserUpdateView.as_view(), name='update_info'),

    # /my/delete/
    path('delete/', UserDeleteView.as_view(), name='delete_account'),
]
