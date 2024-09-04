from rest_framework import serializers
from .models import Korisnik, UposljenaJedinica, PomocniRadnici, Lokacije, EksterniOglasivaci, Steta

class KorisnikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Korisnik
        fields = '__all__'

class UposljenaJedinicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UposljenaJedinica
        fields = '__all__'

class PomocniRadniciSerializer(serializers.ModelSerializer):
    class Meta:
        model = PomocniRadnici
        fields = '__all__'

class LokacijeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lokacije
        fields = '__all__'

class EksterniOglasivaciSerializer(serializers.ModelSerializer):
    class Meta:
        model = EksterniOglasivaci
        fields = '__all__'

class StetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Steta
        fields = '__all__'
