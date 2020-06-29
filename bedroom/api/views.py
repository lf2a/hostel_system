# django rest framework
from rest_framework import viewsets
from rest_framework import response

# local django
from bedroom.models import Bedroom
from bedroom.api.serializers import BedroomSerializer


class BedroomViewSet(viewsets.ModelViewSet):
    queryset = Bedroom.objects.filter(is_available=True)
    serializer_class = BedroomSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.is_available:
            serializer = self.get_serializer(instance)
            return response.Response(serializer.data)
        else:
            return response.Response(status=404)

    def create(self, request, *args, **kwargs):
        return response.Response(status=405)

    def update(self, request, *args, **kwargs):
        return response.Response(status=405)

    def partial_update(self, request, *args, **kwargs):
        return response.Response(status=405)

    def destroy(self, request, *args, **kwargs):
        return response.Response(status=405)
