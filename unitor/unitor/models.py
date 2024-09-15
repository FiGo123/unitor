from django.db import models


class Korisnik(models.Model):
    unique_id = models.AutoField(primary_key=True)
    # Add other fields as required





class Steta(models.Model):
    unique_id = models.AutoField(primary_key=True)
    lokacija = models.ForeignKey(Lokacije, related_name='stete', on_delete=models.CASCADE)
    uposljena_jedinica = models.ForeignKey(UposljenaJedinica, related_name='stete', on_delete=models.CASCADE)
    # Add other fields as required
