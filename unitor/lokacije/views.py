from rest_framework import viewsets
from models import Lokacije
from serializers import LokacijeSerializer

class LokacijeViewSet(viewsets.ModelViewSet):
    queryset = Lokacije.objects.all()
    serializer_class = LokacijeSerializer