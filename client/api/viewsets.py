# django
from django.core import serializers

# django rest framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_405_METHOD_NOT_ALLOWED,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# local django
from client.models import User, Notification
from .serializers import UserSerializer, NotificationSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def list(self, request, *args, **kwrags):
        user = request.user

        data = {
            'user': {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'phone1': user.phone1,
                'phone2': user.phone2,
            }
        }
        return Response(data=data, status=HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        user = request.user
        user_param = kwargs.get('pk')

        if str(user.id) == user_param:
            data = {
                'user': {
                    'id': user.id,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'email': user.email,
                    'phone1': user.phone1,
                    'phone2': user.phone2,
                }
            }
            return Response(data=data, status=HTTP_200_OK)
        else:
            data = {
                'error': {
                    'code': 404,
                    'message': 'Not Found'
                }
            }
            return Response(data=data, status=HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        logged_user = str(request.user.id)
        user_param = kwargs.get('pk')

        if logged_user == user_param:
            return super(UserViewSet, self).update(request, *args, **kwargs)
        else:
            data = {
                'error': {
                    'code': 404,
                    'message': 'Not Found'
                }
            }
            return Response(data=data, status=HTTP_404_NOT_FOUND)

    def partial_update(self, request, *args, **kwargs):
        logged_user = str(request.user.id)
        user_param = kwargs.get('pk')

        if logged_user == user_param:
            return super(UserViewSet, self).partial_update(request, *args, **kwargs)
        else:
            data = {
                'error': {
                    'code': 404,
                    'message': 'Not Found'
                }
            }
            return Response(data=data, status=HTTP_404_NOT_FOUND)

    def destroy(self, request, *args, **kwargs):
        logged_user = str(request.user.id)
        user_param = kwargs.get('pk')

        if logged_user == user_param:
            return super(UserViewSet, self).destroy(request, *args, **kwargs)
        else:
            data = {
                'error': {
                    'code': 404,
                    'message': 'Not Found'
                }
            }
            return Response(data=data, status=HTTP_404_NOT_FOUND)


class NotificationViewSet(ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def list(self, request, *args, **kwrags):
        user = request.user
        self.queryset = Notification.objects.filter(client__id=user.id)
        res = NotificationSerializer(self.queryset, many=True)
        return Response(res.data)

    def retrieve(self, request, *args, **kwargs):
        not_id = kwargs.get('pk')
        notification = Notification.objects.get(id=not_id)

        user = request.user
        client = notification.client

        if user.id == client.id:
            res = NotificationSerializer(notification)
            return Response(res.data)
        else:
            data = {
                'error': {
                    'code': 404,
                    'message': 'Not Found'
                }
            }
            return Response(data=data, status=HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        data = {
            'error': {
                'code': 404,
                'message': 'Not Found'
            }
        }
        return Response(data=data, status=HTTP_404_NOT_FOUND)

    def partial_update(self, request, *args, **kwargs):
        data = {
            'error': {
                'code': 404,
                'message': 'Not Found'
            }
        }
        return Response(data=data, status=HTTP_404_NOT_FOUND)

    def destroy(self, request, *args, **kwargs):
        data = {
            'error': {
                'code': 404,
                'message': 'Not Found'
            }
        }
        return Response(data=data, status=HTTP_404_NOT_FOUND)
