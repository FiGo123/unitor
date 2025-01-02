from django.db import models

class Lokacije(models.Model):
    unique_id = models.AutoField(primary_key=True)  # Unique identifier for each location
    name = models.CharField(max_length=255, unique=True)  # Name of the location
    address = models.TextField(null=True, blank=True)  # Address of the location
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)  # Latitude for geolocation
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)  # Longitude for geolocation
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the record was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for when the record was last updated

    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"
        ordering = ['name']  # Default ordering for querysets

    def __str__(self):
        return self.name