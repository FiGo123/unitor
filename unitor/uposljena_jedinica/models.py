from django.db import models

from unitor.unitor.models import Korisnik


class UposljenaJedinica(models.Model):
    unique_id = models.AutoField(primary_key=True)
    korisnik = models.ForeignKey(Korisnik, related_name='uposljene_jedinice', on_delete=models.CASCADE)
    # Add other fields as required

