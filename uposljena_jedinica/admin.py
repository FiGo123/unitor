from django.contrib import admin
from .models import UposljenaJedinica, Steta
from .models import Tip

admin.site.register(UposljenaJedinica)
admin.site.register(Tip)
admin.site.register(Steta)