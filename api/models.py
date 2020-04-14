from django.db import models

class Accounts(models.Model):
    id = models.UUIDField(primary_key=True)
    email = models.TextField(unique=True)
    mobn = models.TextField(unique=True)
    agent = models.TextField()
    contract = models.TextField(blank=True, null=True)
    status = models.BooleanField()
    type = models.TextField()
    tag = models.TextField(blank=True, null=True)
    region = models.ForeignKey('Regions', models.CASCADE)
    currency = models.ForeignKey('Currencies', models.CASCADE)
    trust_limit = models.BigIntegerField(null=True)
    limit_per_transaction = models.BigIntegerField(null=True)
    limit_per_day = models.BigIntegerField(null=True)

    class Meta:
        db_table = 'accounts'


class Currencies(models.Model):
    id = models.UUIDField(primary_key=True)
    iso_code = models.IntegerField()
    ticker = models.TextField()
    description = models.TextField()
    region = models.ForeignKey('Regions', models.CASCADE)

    class Meta:
        db_table = 'currencies'


class Regions(models.Model):
    id = models.UUIDField(primary_key=True)
    code = models.TextField()
    description = models.TextField()

    class Meta:
        db_table = 'regions'
