from django.db import models
from lokacije.models import Lokacije


class Korisnik(models.Model):
    unique_id = models.AutoField(primary_key=True)
    # Add other fields as required


