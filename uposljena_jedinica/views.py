from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated
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
    serializer_class = UposljenaJedinicaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = UposljenaJedinicaFilter
    permission_classes = [IsAuthenticated]  # Ensures only authenticated users can access this view

    def get_queryset(self):
        """
        Return only the UposljenaJedinica records related to the logged-in user.
        """
        return UposljenaJedinica.objects.filter(korisnik=self.request.user)


class StetaViewSet(viewsets.ModelViewSet):
    queryset = Steta.objects.all()
    serializer_class = StetaSerializer