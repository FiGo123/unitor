from django.db import models

from unitor.unitor.models import UposljenaJedinica


class PomocniRadnici(models.Model):
    unique_id = models.AutoField(primary_key=True)
    uposljena_jedinica = models.ForeignKey(UposljenaJedinica, related_name='pomocni_radnici', on_delete=models.CASCADE)
    # Add other fields as required