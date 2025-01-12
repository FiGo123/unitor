from rest_framework import viewsets

from uposljena_jedinica.models import UposljenaJedinica
from uposljena_jedinica.serializers import UposljenaJedinicaSerializer


class UposljenaJedinicaViewSet(viewsets.ModelViewSet):
    print("projaa")
    try:
        queryset = UposljenaJedinica.objects.all()
    except Exception as e:
        print("paradox")
        print(e)
    serializer_class = UposljenaJedinicaSerializer

