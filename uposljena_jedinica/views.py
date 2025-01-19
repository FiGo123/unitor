from rest_framework import viewsets

from uposljena_jedinica.models import UposljenaJedinica, Steta
from uposljena_jedinica.serializers import UposljenaJedinicaSerializer, StetaSerializer
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, DateFilter

class UposljenaJedinicaFilter(FilterSet):
    iznajmljeno_od = DateFilter(field_name="detalji_iznajmljivanja__iznajmljeno_od", lookup_expr="gte")
    iznajmljeno_do = DateFilter(field_name="detalji_iznajmljivanja__iznajmljeno_do", lookup_expr="lte")

    class Meta:
        model = UposljenaJedinica
        fields = ['iznajmljeno_od', 'iznajmljeno_do']

class UposljenaJedinicaViewSet(viewsets.ModelViewSet):
    queryset = UposljenaJedinica.objects.all()
    serializer_class = UposljenaJedinicaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = UposljenaJedinicaFilter


class StetaViewSet(viewsets.ModelViewSet):
    queryset = Steta.objects.all()
    serializer_class = StetaSerializer