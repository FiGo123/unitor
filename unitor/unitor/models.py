from django.db import models


class Korisnik(models.Model):
    unique_id = models.AutoField(primary_key=True)
    # Add other fields as required


class UposljenaJedinica(models.Model):
    unique_id = models.AutoField(primary_key=True)
    korisnik = models.ForeignKey(Korisnik, related_name='uposljene_jedinice', on_delete=models.CASCADE)
    # Add other fields as required


class PomocniRadnici(models.Model):
    unique_id = models.AutoField(primary_key=True)
    uposljena_jedinica = models.ForeignKey(UposljenaJedinica, related_name='pomocni_radnici', on_delete=models.CASCADE)
    # Add other fields as required




class EksterniOglasivaci(models.Model):
    unique_id = models.AutoField(primary_key=True)
    korisnik = models.ForeignKey(Korisnik, related_name='eksterni_oglasivaci', on_delete=models.CASCADE)
    # Add other fields as required


class Steta(models.Model):
    unique_id = models.AutoField(primary_key=True)
    lokacija = models.ForeignKey(Lokacije, related_name='stete', on_delete=models.CASCADE)
    uposljena_jedinica = models.ForeignKey(UposljenaJedinica, related_name='stete', on_delete=models.CASCADE)
    # Add other fields as required
