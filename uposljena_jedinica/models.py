from django.db import models


class UposljenaJedinica(models.Model):
    unique_id = models.AutoField(primary_key=True)
    korisnik = models.ForeignKey('unitor.Korisnik', related_name='uposljene_jedinice', on_delete=models.CASCADE)
    tip = models.ForeignKey(
        'Tip',
        related_name='uposljene_jedinice',
        on_delete=models.SET_NULL,
        null=True,  # Allow null if no type is assigned
        blank=True
    )
    # Add other fields as required


class Tip(models.Model):
    id = models.AutoField(primary_key=True)
    naziv = models.CharField(max_length=255, unique=True)  # Name of the type (e.g., Car, Yacht, House)
    opis = models.TextField(blank=True, null=True)  # Optional description for the type

    def __str__(self):
        return self.naziv