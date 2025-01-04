from rest_framework import viewsets

from unitor.eksterni_oglasivaci.models import EksterniOglasivaci
from unitor.eksterni_oglasivaci.serializers import EksterniOglasivaciSerializer


class EksterniOglasivaciViewSet(viewsets.ModelViewSet):
    queryset = EksterniOglasivaci.objects.all()
    serializer_class = EksterniOglasivaciSerializer
