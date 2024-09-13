from rest_framework import viewsets

from unitor.pomocni_radnici.models import PomocniRadnici
from unitor.pomocni_radnici.serializers import PomocniRadniciSerializer


class PomocniRadniciViewSet(viewsets.ModelViewSet):
    queryset = PomocniRadnici.objects.all()
    serializer_class = PomocniRadniciSerializer
