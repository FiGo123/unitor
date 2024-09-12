from django.db import models

class Lokacije(models.Model):
    unique_id = models.AutoField(primary_key=True)
    # Add other fields as required