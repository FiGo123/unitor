from rest_framework import serializers
from unitor.uposljena_jedinica.models import UposljenaJedinica


class UposljenaJedinicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UposljenaJedinica
        fields = '__all__'

    # Field-level validation example for 'unit_name'
    def validate_unit_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Unit name must be at least 3 characters long.")
        return value

