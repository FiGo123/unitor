from rest_framework import viewsets

from .models import Korisnik, Steta
from .serializers import KorisnikSerializer, StetaSerializer


class KorisnikViewSet(viewsets.ModelViewSet):
    queryset = Korisnik.objects.all()
    serializer_class = KorisnikSerializer


class StetaViewSet(viewsets.ModelViewSet):
    queryset = Steta.objects.all()
    serializer_class = StetaSerializer