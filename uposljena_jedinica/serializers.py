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

    def validate(self, data):
        """
        Ensure no overlapping rentals exist for the same unit on the same day.
        """
        print("validejsn")
        jedinica = data.get('jedinica')
        iznajmljeno_od = data.get('iznajmljeno_od')
        iznajmljeno_do = data.get('iznajmljeno_do')

        if iznajmljeno_od and iznajmljeno_do and iznajmljeno_od > iznajmljeno_do:
            raise serializers.ValidationError("'iznajmljeno_od' cannot be after 'iznajmljeno_do'.")

        # Query for overlapping rentals for the same jedinica
        overlapping_rentals = DetaljiIznajmljivanja.objects.filter(
            jedinica=jedinica,
            iznajmljeno_od__lte=iznajmljeno_do,
            iznajmljeno_do__gte=iznajmljeno_od
        )

        # Exclude the current instance in case of updates
        if self.instance:
            overlapping_rentals = overlapping_rentals.exclude(pk=self.instance.pk)

        if overlapping_rentals.exists():
            raise serializers.ValidationError("There is already a rental for this unit in the specified date range.")

        return data


class UposljenaJedinicaSerializer(serializers.ModelSerializer):
    detalji_iznajmljivanja = DetaljiIznajmljivanjaSerializer(many=True, read_only=True)

    class Meta:
        model = UposljenaJedinica
        fields = '__all__'

    def validate_naziv(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Naziv mora imati najmanje 3 karaktera.")
        return value


