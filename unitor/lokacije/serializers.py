from rest_framework import serializers


class LokacijeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lokacije
        fields = '__all__'

    # Field-level validation for 'city'
    def validate_city(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("City name must contain only letters.")
        return value
