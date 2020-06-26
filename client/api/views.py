# django rest framework
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

# local django
from client.api.serializers import UserSerializer


class UserView(generics.RetrieveUpdateDestroyAPIView):
    """Get user info, update user info and 'delete' user"""
    
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
