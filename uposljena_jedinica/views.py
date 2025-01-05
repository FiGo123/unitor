from rest_framework import viewsets

from uposljena_jedinica.models import UposljenaJedinica
from uposljena_jedinica.serializers import UposljenaJedinicaSerializer


class UposljenaJedinicaViewSet(viewsets.ModelViewSet):
    queryset = UposljenaJedinica.objects.all()
    serializer_class = UposljenaJedinicaSerializer

