from django.db import models


class UposljenaJedinica(models.Model):
    unique_id = models.AutoField(primary_key=True)
    korisnik = models.ForeignKey('unitor.Korisnik', related_name='uposljene_jedinice', on_delete=models.CASCADE)
    # Add other fields as required
