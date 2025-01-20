from django.db import models

from unitor.models import Korisnik


class Platforma(models.Model):
    name = models.CharField(max_length=100, unique=True)  # npr. "Airbnb", "Booking.com"

    def __str__(self):
        return self.name

class EksterniOglasivaci(models.Model):
    unique_id = models.AutoField(primary_key=True)
    korisnik = models.ForeignKey(Korisnik, related_name='eksterni_oglasivaci', on_delete=models.CASCADE)

    platform = models.ForeignKey(Platforma, related_name='eksterni_oglasivaci', on_delete=models.CASCADE)
    api_key = models.CharField(max_length=255)
    last_sync = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('korisnik', 'platform')  # Svaki korisnik može imati jedan ključ po platformi
        verbose_name = "Eksterni Oglasivač"
        verbose_name_plural = "Eksterni Oglasivači"

    def __str__(self):
        return f"{self.korisnik} - {self.platform}"