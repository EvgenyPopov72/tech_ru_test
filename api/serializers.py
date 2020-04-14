from rest_framework import serializers

from api.models import Regions, Currencies, Accounts


class RegionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Regions
        exclude = []


class CurrenciesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Currencies
        exclude = []

class AccountsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Accounts
        exclude = []
