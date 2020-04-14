from rest_framework import viewsets

from api.models import Currencies, Regions, Accounts
from api.serializers import RegionsSerializer, CurrenciesSerializer, AccountsSerializer


class RegionsViewSet(viewsets.ModelViewSet):
    queryset = Regions.objects.all()
    serializer_class = RegionsSerializer


class CurrenciesViewSet(viewsets.ModelViewSet):
    queryset = Currencies.objects.all()
    serializer_class = CurrenciesSerializer

class AccountsViewSet(viewsets.ModelViewSet):
    queryset = Accounts.objects.all()
    serializer_class = AccountsSerializer
