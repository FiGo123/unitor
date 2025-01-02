from django.db import models

from unitor.lokacije.models import Lokacije
from unitor.uposljena_jedinica.models import UposljenaJedinica


class Korisnik(models.Model):
    unique_id = models.AutoField(primary_key=True)
    # Add other fields as required





class Steta(models.Model):
    unique_id = models.AutoField(primary_key=True)
    lokacija = models.ForeignKey(Lokacije, related_name='stete', on_delete=models.CASCADE)
    uposljena_jedinica = models.ForeignKey(UposljenaJedinica, related_name='stete', on_delete=models.CASCADE)
    # Add other fields as required
