import uuid as g_uuid
from django.db import models

from sales.helpers.date import format_date
from sales.helpers.money import decimal_to_abbreviate, abbreviate_to_decimal
from sales.models.base import BaseBlank


class AreaUnitModel(models.Model):
    uuid = models.UUIDField(default=g_uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        app_label = "sales"


class CityModel(models.Model):
    uuid = models.UUIDField(default=g_uuid.uuid4, editable=False, unique=True)
    name = models.CharField(unique=True, max_length=255)
    state = models.CharField(max_length=2)

    class Meta:
        app_label = "sales"


class HomeTypeModel(models.Model):
    uuid = models.UUIDField(default=g_uuid.uuid4, editable=False, unique=True)
    type = models.CharField(unique=True, max_length=255)

    class Meta:
        app_label = "sales"


class PriceHistoryModel(BaseBlank, models.Model):
    uuid = models.UUIDField(default=g_uuid.uuid4, editable=False, unique=True)
    sell_price = models.DecimalField(decimal_places=2, max_digits=15)
    rent_price = models.DecimalField(decimal_places=2, blank=True, null=True, max_digits=15)  # noqa
    last_sold_date = models.DateField(null=True)
    last_sold_price = models.DecimalField(decimal_places=2, null=True, max_digits=15)  # noqa

    @property
    def abbreviate_price(self):
        return decimal_to_abbreviate(float(self.sell_price))

    class Meta:
        app_label = "sales"

    class CustomMeta:
        blank_together = ('last_sold_date', 'last_sold_price')


class TaxModel(models.Model):
    uuid = models.UUIDField(default=g_uuid.uuid4, editable=False, unique=True)
    tax_value = models.DecimalField(decimal_places=2, max_digits=15)
    tax_year = models.IntegerField()

    class Meta:
        app_label = "sales"


class ResidenceModel(models.Model):
    uuid = models.UUIDField(default=g_uuid.uuid4, editable=False, unique=True)
    city = models.ForeignKey('CityModel', on_delete=models.CASCADE)
    area_unit = models.ForeignKey('AreaUnitModel', on_delete=models.CASCADE)
    address = models.CharField(max_length=500)
    bathrooms = models.DecimalField(decimal_places=2, max_digits=15, null=True)  # noqa
    bedrooms = models.IntegerField(null=False)
    home_size = models.IntegerField(null=True)
    home_type = models.ForeignKey('HomeTypeModel', on_delete=models.CASCADE)
    property_size = models.IntegerField(null=True)
    year_built = models.IntegerField(null=True)

    class Meta:
        app_label = "sales"


class ZRentInformationModel(models.Model):
    uuid = models.UUIDField(default=g_uuid.uuid4, editable=False, unique=True)
    rentzestimate_amount = models.DecimalField(decimal_places=2, max_digits=15)
    rentzestimate_last_updated = models.DateField(auto_now=True, blank=True, null=True)  # noqa

    class Meta:
        app_label = "sales"


class ZSaleInformationModel(models.Model):
    uuid = models.UUIDField(default=g_uuid.uuid4, editable=False, unique=True)
    zestimate_last_updated = models.DateField(auto_now=True)
    zestimate_amount = models.DecimalField(decimal_places=2, max_digits=15)

    class Meta:
        app_label = "sales"


class ZillowModel(models.Model):
    uuid = models.UUIDField(default=g_uuid.uuid4, editable=False, unique=True)
    zillow_id = models.IntegerField(unique=True)
    z_rent_information = models.ForeignKey('ZRentInformationModel', on_delete=models.CASCADE)  # noqa
    z_sale_information = models.ForeignKey('ZSaleInformationModel', on_delete=models.CASCADE)  # noqa

    class Meta:
        app_label = "sales"


class AnnouncementModel(models.Model):
    uuid = models.UUIDField(default=g_uuid.uuid4, editable=False, unique=True)
    zillow = models.ForeignKey('ZillowModel', on_delete=models.CASCADE)
    price_history = models.ManyToManyField('PriceHistoryModel')
    link = models.CharField(max_length=1000)
    residence = models.ForeignKey('ResidenceModel', on_delete=models.CASCADE)
    tax = models.ForeignKey('TaxModel', on_delete=models.CASCADE)

    @classmethod
    def import_data(cls, payload):
        """
        It's a function to import data using entities get_or_create
        """
        city = {
            "name": payload.get('city'),
            "state": payload.get('state')
        }
        area_unit = {
            "name": payload.get('area_unit'),
        }
        home_type = {
            "type": payload.get('home_type')
        }
        residence = {
            "city": CityModel.objects.get_or_create(**city)[0],
            "area_unit": AreaUnitModel.objects.get_or_create(**area_unit)[0],  # noqa
            "address": payload.get('address'),
            "bathrooms": payload.get('bathrooms') if payload.get('bathrooms') else None,  # noqa
            "bedrooms": payload.get('bedrooms'),
            "home_size": payload.get('home_size') if payload.get('home_size') else None,  # noqa
            "home_type": HomeTypeModel.objects.get_or_create(**home_type)[0],  # noqa
            "property_size": payload.get('property_size') if payload.get('property_size') else None,  # noqa
            "year_built": payload.get('year_built') if payload.get('year_built') else None,  # noqa

        }
        price_history = {
            "sell_price": abbreviate_to_decimal(payload.get('price')),
            "rent_price": float(payload.get('rent_price')) if payload.get('rent_price') else None,  # noqa
            "last_sold_date": format_date(payload.get('last_sold_date')),
            "last_sold_price": float(payload.get('last_sold_price')) if payload.get('last_sold_price') else None,  # noqa
        }
        z_sale_information = {
            "zestimate_last_updated": format_date(payload.get('zestimate_last_updated')),  # noqa
            "zestimate_amount": float(payload.get('zestimate_amount')) if payload.get('zestimate_amount') else 0,  # noqa
        }
        z_rent_information = {
            "rentzestimate_amount": float(payload.get('rentzestimate_amount')) if payload.get('rentzestimate_amount') else 0,  # noqa
            "rentzestimate_last_updated": format_date(payload.get('rentzestimate_last_updated')),  # noqa
        }
        tax = {
            "tax_value": float(payload.get('tax_value')),
            "tax_year": payload.get('tax_year')
        }

        zillow = {
            "zillow_id": int(payload.get('zillow_id')),
            "z_rent_information": ZRentInformationModel.objects.get_or_create(**z_rent_information)[0],  # noqa
            "z_sale_information": ZSaleInformationModel.objects.get_or_create(**z_sale_information)[0],  # noqa
        }
        zillow = ZillowModel.objects.get_or_create(**zillow)[0]

        residence = ResidenceModel.objects.get_or_create(**residence)[0]
        tax = TaxModel.objects.get_or_create(**tax)[0]
        price_history = PriceHistoryModel.objects.get_or_create(**price_history)[0]  # noqa
        announcement = cls.objects.get_or_create(link=payload.get('link'),
                                                               zillow=zillow,
                                                               residence=residence,  # noqa
                                                               tax=tax)[0]  # noqa
        announcement.price_history.add(price_history)

        return announcement

    class Meta:
        app_label = "sales"
