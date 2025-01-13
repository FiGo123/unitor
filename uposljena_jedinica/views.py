from rest_framework import viewsets

from uposljena_jedinica.models import UposljenaJedinica, Steta
from uposljena_jedinica.serializers import UposljenaJedinicaSerializer, StetaSerializer


class UposljenaJedinicaViewSet(viewsets.ModelViewSet):
    print("projaa")
    try:
        queryset = UposljenaJedinica.objects.all()
    except Exception as e:
        print("paradox")
        print(e)
    serializer_class = UposljenaJedinicaSerializer


class StetaViewSet(viewsets.ModelViewSet):
    queryset = Steta.objects.all()
    serializer_class = StetaSerializer