# django
from django.contrib.auth import get_user_model
from django.db import IntegrityError

# django rest framework
from rest_framework import viewsets
from rest_framework import response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout


class SignUpViewSet(viewsets.ModelViewSet):

    def create(self, request, *args, **kwargs):
        email = request.data.get('email', False)
        password = request.data.get('password', False)

        if email or password:
            try:
                user = get_user_model().objects.create_user(**request.data)
                token = Token.objects.create(user=user)
                return response.Response(data={'token': token.key}, status=201)
            except IntegrityError:
                data = {'msg': 'Um ou mais campos invalidos. Username ou email já existe.'}
                return response.Response(data=data, status=400)
        return response.Response(status=400)

    def list(self, request, *args, **kwargs):
        return response.Response(status=405)

    def retrieve(self, request, *args, **kwargs):
        return response.Response(status=405)

    def destroy(self, request, *args, **kwargs):
        return response.Response(status=405)

    def update(self, request, *args, **kwargs):
        return response.Response(status=404)

    def partial_update(self, request, *args, **kwargs):
        return response.Response(status=404)


class LogoutViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        logout(request)
        return response.Response(status=201)

    def list(self, request, *args, **kwargs):
        return response.Response(status=405)

    def retrieve(self, request, *args, **kwargs):
        return response.Response(status=405)

    def destroy(self, request, *args, **kwargs):
        return response.Response(status=405)

    def update(self, request, *args, **kwargs):
        return response.Response(status=404)

    def partial_update(self, request, *args, **kwargs):
        return response.Response(status=404)
