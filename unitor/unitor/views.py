from rest_framework import viewsets
from .models import Korisnik, UposljenaJedinica, PomocniRadnici, Lokacije, EksterniOglasivaci, Steta
from .serializers import KorisnikSerializer, UposljenaJedinicaSerializer, PomocniRadniciSerializer, LokacijeSerializer, EksterniOglasivaciSerializer, StetaSerializer

class KorisnikViewSet(viewsets.ModelViewSet):
    queryset = Korisnik.objects.all()
    serializer_class = KorisnikSerializer


class StetaViewSet(viewsets.ModelViewSet):
    queryset = Steta.objects.all()
    serializer_class = StetaSerializer