from rest_framework import viewsets

from pomocni_radnici.models import PomocniRadnici
from pomocni_radnici.serializers import PomocniRadniciSerializer


class PomocniRadniciViewSet(viewsets.ModelViewSet):
    queryset = PomocniRadnici.objects.all()
    serializer_class = PomocniRadniciSerializer
