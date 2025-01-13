from rest_framework import serializers

from unitor.models import Korisnik


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



