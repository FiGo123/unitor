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
