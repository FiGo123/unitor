from django.core.exceptions import ValidationError
from django.db import models

from lokacije.models import Lokacije


class UposljenaJedinica(models.Model):
    unique_id = models.AutoField(primary_key=True)
    naziv = models.CharField(max_length=255, default=None, null=True,
    blank=True)
    cijena_prednajma = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    korisnik = models.ForeignKey('unitor.Korisnik', related_name='uposljene_jedinice', on_delete=models.CASCADE)
    lokacija = models.ForeignKey(
    'lokacije.Lokacije',
    related_name='uposljene_jedinice',
    on_delete=models.CASCADE,
    default=None,
    null=True,
    blank=True
)

    tip = models.ForeignKey(
        'Tip',
        related_name='uposljena_jedinice',
        on_delete=models.SET_NULL,
        null=True,  # Allow null if no type is assigned
        blank=True
    )
    pomocni_radnici = models.ForeignKey(
        'PomocniRadnici',
        related_name='uposljena_jedinice',
        on_delete=models.SET_NULL,
        null=True,  # Allow null if no type is assigned
        blank=True
    )
    # Add other fields as required




    def __str__(self):
        return f"Uposljena Jedinica {self.unique_id} -  {self.tip} - {self.korisnik} - {self.lokacija}"


class Tip(models.Model):
    id = models.AutoField(primary_key=True)
    naziv = models.CharField(max_length=255, unique=True)  # Name of the type (e.g., Car, Yacht, House)
    opis = models.TextField(blank=True, null=True)  # Optional description for the type

    def __str__(self):
        return self.naziv

class Steta(models.Model):
    unique_id = models.AutoField(primary_key=True)
    naziv = models.CharField(max_length=255, default=None, null=True,
                             blank=True)
    opis = models.TextField(blank=True, null=True)
    detalji_iznajmljivanja = models.ForeignKey('uposljena_jedinica.DetaljiIznajmljivanja', related_name='stete', on_delete=models.CASCADE)

class PomocniRadnici(models.Model):
    id = models.AutoField(primary_key=True)
    naziv = models.CharField(max_length=255, unique=True)  # Name of the type (e.g., Car, Yacht, House)

    def __str__(self):
        return self.naziv
    # Add other fields as required


class DetaljiIznajmljivanja(models.Model):
    jedinica = models.ForeignKey(
        'UposljenaJedinica',
        related_name='detalji_iznajmljivanja',
        on_delete=models.CASCADE
    )
    iznajmljena = models.BooleanField(default=False)
    cijena = models.DecimalField(max_digits=10, decimal_places=2)
    tip_iznajmljivanja = models.CharField(
        max_length=50,
        choices=[('mjesecno', 'Mjesecno'), ('dnevno', 'Dnevno')]
    )
    iznajmljeno_od = models.DateField(null=True, blank=True)
    iznajmljeno_do = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Detalji Iznajmljivanja za {self.jedinica}"

    def clean(self):
        super().clean()

        if self.iznajmljeno_od and self.iznajmljeno_do and self.iznajmljeno_od > self.iznajmljeno_do:
            raise ValidationError("'iznajmljeno_od' cannot be after 'iznajmljeno_do'.")

        # Check for overlapping rentals
        overlapping_rentals = DetaljiIznajmljivanja.objects.filter(
            jedinica=self.jedinica,
            iznajmljeno_od__lt=self.iznajmljeno_do,
            iznajmljeno_do__gt=self.iznajmljeno_od
        ).exclude(pk=self.pk)  # Exclude the current instance during updates

        if overlapping_rentals.exists():
            raise ValidationError("There is already a rental for this unit in the specified date range.")

        # Check for exact duplicates
        exact_duplicate = DetaljiIznajmljivanja.objects.filter(
            jedinica=self.jedinica,
            iznajmljeno_od=self.iznajmljeno_od,
            iznajmljeno_do=self.iznajmljeno_do
        ).exclude(pk=self.pk)  # Exclude the current instance during updates

        if exact_duplicate.exists():
            raise ValidationError("A rental with the exact same dates already exists for this unit.")

    def save(self, *args, **kwargs):
        self.full_clean()  # Call the clean method before saving
        super().save(*args, **kwargs)