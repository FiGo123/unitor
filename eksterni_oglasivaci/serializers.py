from rest_framework import serializers

from unitor.eksterni_oglasivaci.models import EksterniOglasivaci


class EksterniOglasivaciSerializer(serializers.ModelSerializer):
    class Meta:
        model = EksterniOglasivaci
        fields = '__all__'

    # Field-level validation for 'advertiser_name'
    def validate_advertiser_name(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Advertiser name must be at least 5 characters long.")
        return value