from rest_framework import viewsets
from .models import Korisnik, UposljenaJedinica, PomocniRadnici, Lokacije, EksterniOglasivaci, Steta
from .serializers import KorisnikSerializer, UposljenaJedinicaSerializer, PomocniRadniciSerializer, LokacijeSerializer, EksterniOglasivaciSerializer, StetaSerializer

class KorisnikViewSet(viewsets.ModelViewSet):
    queryset = Korisnik.objects.all()
    serializer_class = KorisnikSerializer

class UposljenaJedinicaViewSet(viewsets.ModelViewSet):
    queryset = UposljenaJedinica.objects.all()
    serializer_class = UposljenaJedinicaSerializer

class PomocniRadniciViewSet(viewsets.ModelViewSet):
    queryset = PomocniRadnici.objects.all()
    serializer_class = PomocniRadniciSerializer



class EksterniOglasivaciViewSet(viewsets.ModelViewSet):
    queryset = EksterniOglasivaci.objects.all()
    serializer_class = EksterniOglasivaciSerializer

class StetaViewSet(viewsets.ModelViewSet):
    queryset = Steta.objects.all()
    serializer_class = StetaSerializer