from django.contrib import admin
from .models import UposljenaJedinica, Steta, DetaljiIznajmljivanja, PomocniRadnici
from .models import Tip

admin.site.register(UposljenaJedinica)
admin.site.register(Tip)
admin.site.register(Steta)
admin.site.register(DetaljiIznajmljivanja)
admin.site.register(PomocniRadnici)


#TODO Validacije da se ne mogu preklapati datumi
#TODO Filteri za vrijeme, cijene
#TODO Da se dodaju slike za jedinice, stetu(nije bitan task)
