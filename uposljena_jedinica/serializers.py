from rest_framework import serializers
from uposljena_jedinica.models import UposljenaJedinica, Steta, DetaljiIznajmljivanja


class StetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Steta
        fields = '__all__'

    # Object-level validation
    def validate(self, data):
        if data['amount'] < 0:
            raise serializers.ValidationError("Iznos štete ne može biti negativan.")
        return data


class DetaljiIznajmljivanjaSerializer(serializers.ModelSerializer):
    stete = StetaSerializer(many=True, read_only=True)  # Assuming a `related_name` "stete" on Steta model

    class Meta:
        model = DetaljiIznajmljivanja
        fields = '__all__'


class UposljenaJedinicaSerializer(serializers.ModelSerializer):
    detalji_iznajmljivanja = DetaljiIznajmljivanjaSerializer(many=True, read_only=True)

    class Meta:
        model = UposljenaJedinica
        fields = '__all__'

    def validate_naziv(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Naziv mora imati najmanje 3 karaktera.")
        return value
