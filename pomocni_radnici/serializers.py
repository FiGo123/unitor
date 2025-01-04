from rest_framework import serializers

from unitor.pomocni_radnici.models import PomocniRadnici


class PomocniRadniciSerializer(serializers.ModelSerializer):
    class Meta:
        model = PomocniRadnici
        fields = '__all__'

    # Object-level validation
    def validate(self, data):
        if data['hours_worked'] < 0:
            raise serializers.ValidationError("Hours worked cannot be negative.")
        return data
