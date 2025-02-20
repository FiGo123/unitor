from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated
from uposljena_jedinica.models import UposljenaJedinica, Steta, DetaljiIznajmljivanja
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
    serializer_class = StetaSerializer
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can access

    def get_queryset(self):
        # Get the currently authenticated user
        user = self.request.user

        # Get all uposljena_jedinica associated with the user
        user_units = UposljenaJedinica.objects.filter(korisnik=user)

        # Get the related detalji_iznajmljivanja instances
        user_rentals = DetaljiIznajmljivanja.objects.filter(jedinica__in=user_units)

        # Filter Steta records that are associated with these rentals
        return Steta.objects.filter(detalji_iznajmljivanja__in=user_rentals)

