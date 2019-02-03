import uuid as g_uuid
from django.db import models


class AreaUnit(models.Model):
    uuid = models.UUIDField(default=g_uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255, null=False, unique=True)


class City(models.Model):
    uuid = models.UUIDField(default=g_uuid.uuid4, editable=False, unique=True)
    name = models.CharField(unique=True, null=False)
    state = models.CharField(max_length=2, null=False)


class HomeType(models.Model):
    uuid = models.UUIDField(default=g_uuid.uuid4, editable=False, unique=True)
    type = models.CharField(unique=True, null=False)


class PriceHistory(models.Model):
    uuid = models.UUIDField(default=g_uuid.uuid4, editable=False, unique=True)
    sell_price = models.DecimalField(decimal_places=2)
    rent_price = models.DecimalField(decimal_places=2, blank=True, null=True)
    last_sold_date = models.DateField(null=True)
    last_sold_price = models.IntegerField(null=True)


class Tax(models.Model):
    uuid = models.UUIDField(default=g_uuid.uuid4, editable=False, unique=True)
    tax_value = models.DecimalField(decimal_places=2)
    tax_year = models.IntegerField(max_length=4)


class Residence(models.Model):
    uuid = models.UUIDField(default=g_uuid.uuid4, editable=False, unique=True)
    city = models.ForeignKey('City')
    area_unit = models.ForeignKey('AreaUnit')
    address = models.CharField(max_length=500, null=False)
    bathrooms = models.DecimalField(decimal_places=2, null=True, blank=True)
    bedrooms = models.IntegerField(null=False)
    home_size = models.IntegerField(null=True, blank=True)
    home_type = models.ForeignKey('HomeType')
    property_size = models.IntegerField(null=False)
    year_built = models.IntegerField(max_length=4, blank=True, null=True)


class ZRentInformation(models.Model):
    uuid = models.UUIDField(default=g_uuid.uuid4, editable=False, unique=True)
    rentzestimate_amount = models.DecimalField(decimal_places=2, blank=True, null=True)  # noqa
    rentzestimate_last_updated = models.DateField(auto_now=True, blank=True, null=True)  # noqa


class ZSaleInformation(models.Model):
    uuid = models.UUIDField(default=g_uuid.uuid4, editable=False, unique=True)
    zillow_id = models.IntegerField(unique=True, null=False)
    zestimate_last_updated = models.DateField(auto_now=True)
    zestimate_amount = models.DecimalField(decimal_places=2)


class Zillow(models.Model):
    uuid = models.UUIDField(default=g_uuid.uuid4, editable=False, unique=True)
    zillow_id = models.IntegerField(unique=True, null=False)
    z_rent_information = models.ForeignKey('ZRentInformation')
    z_sale_information = models.ForeignKey('ZSaleInformation')


class Announcement(models.Model):
    uuid = models.UUIDField(default=g_uuid.uuid4, editable=False, unique=True)
    zillow = models.ForeignKey('Zillow')
    price_history = models.ManyToManyField('PriceHistory')
    link = models.CharField(max_length=1000, null=False)
    residence = models.ForeignKey('Residence')
    tax = models.ForeignKey('Tax')

    @property
    def price(self):
        # TODO: You will need to implement the property to convert the decimal value price to abbreviated
        pass
