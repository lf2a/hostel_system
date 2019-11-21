# django
from django.urls import path

# local django
from .views import view_info, notification, get_notification, Delete, UpdateInfo

urlpatterns = [
    # /user/
    path('', view_info, name='user_info'),

    # /user/update/
    # path('update/', update_info, name='update_info'),
    path('update/', UpdateInfo.as_view(), name='update_info'),

    # /user/delete/
    # path('delete/', delete, name='delete'),
    path('delete/', Delete.as_view(), name='delete'),

    # /user/notification/
    path('notification/', notification, name='notifications'),

    # /user/notification/<str:id>
    path('notification/<str:id>', get_notification, name='notification')
]
