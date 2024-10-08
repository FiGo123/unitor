from rest_framework import serializers
from .models import Korisnik, EksterniOglasivaci, Steta

class KorisnikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Korisnik
        fields = '__all__'

    # Field-level validation example for 'email'
    def validate_email(self, value):
        if not value.endswith('@example.com'):
            raise serializers.ValidationError("Email must be under '@example.com' domain.")
        return value

    # Object-level validation
    def validate(self, data):
        if data['age'] < 18:
            raise serializers.ValidationError("Age must be at least 18.")
        return data



class StetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Steta
        fields = '__all__'

    # Object-level validation
    def validate(self, data):
        if data['amount'] < 0:
            raise serializers.ValidationError("Damage amount cannot be negative.")
        return data
