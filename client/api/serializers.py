# django rest framework
from rest_framework.serializers import ModelSerializer

# local django
from client.models import User, Notification


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'phone1',
            'phone2',
            'email'
        ]


class NotificationSerializer(ModelSerializer):
    class Meta:
        model = Notification
        fields = ['client', 'title', 'description', 'created_at']
