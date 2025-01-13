from rest_framework import serializers
from uposljena_jedinica.models import UposljenaJedinica, Steta


class UposljenaJedinicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UposljenaJedinica
        fields = '__all__'

    # Field-level validation example for 'unit_name'
    def validate_unit_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Unit name must be at least 3 characters long.")
        return value


class StetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Steta
        fields = '__all__'

    # Object-level validation
    def validate(self, data):
        if data['amount'] < 0:
            raise serializers.ValidationError("Damage amount cannot be negative.")
        return data
