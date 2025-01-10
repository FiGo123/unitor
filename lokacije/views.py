from rest_framework import viewsets
from lokacije.models import Lokacije
from .serializers import LokacijeSerializer

class LokacijeViewSet(viewsets.ModelViewSet):
    queryset = Lokacije.objects.all()
    serializer_class = LokacijeSerializer

    # Create (POST) method
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return response

    # Update (PUT) method
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return response
