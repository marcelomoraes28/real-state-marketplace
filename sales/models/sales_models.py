import uuid as g_uuid
from django.db import models


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


class PriceHistoryModel(models.Model):
    uuid = models.UUIDField(default=g_uuid.uuid4, editable=False, unique=True)
    sell_price = models.DecimalField(decimal_places=2, max_digits=15)
    rent_price = models.DecimalField(decimal_places=2, blank=True, null=True, max_digits=15)  # noqa
    last_sold_date = models.DateField(null=True, blank=True)
    last_sold_price = models.DecimalField(decimal_places=2, blank=True, null=True, max_digits=15)  # noqa

    class Meta:
        app_label = "sales"


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
    rentzestimate_amount = models.DecimalField(decimal_places=2, max_digits=15, blank=True, null=True)  # noqa
    rentzestimate_last_updated = models.DateField(auto_now=True, blank=True, null=True)  # noqa

    class Meta:
        app_label = "sales"


class ZSaleInformationModel(models.Model):
    uuid = models.UUIDField(default=g_uuid.uuid4, editable=False, unique=True)
    zestimate_last_updated = models.DateField(auto_now=True)
    zestimate_amount = models.DecimalField(decimal_places=2, max_digits=15, null=True)

    class Meta:
        app_label = "sales"


class ZillowModel(models.Model):
    uuid = models.UUIDField(default=g_uuid.uuid4, editable=False, unique=True)
    zillow_id = models.IntegerField(unique=True)
    z_rent_information = models.ForeignKey('ZRentInformationModel', on_delete=models.CASCADE)
    z_sale_information = models.ForeignKey('ZSaleInformationModel', on_delete=models.CASCADE)

    class Meta:
        app_label = "sales"


class AnnouncementModel(models.Model):
    uuid = models.UUIDField(default=g_uuid.uuid4, editable=False, unique=True)
    zillow = models.ForeignKey('ZillowModel', on_delete=models.CASCADE)
    price_history = models.ManyToManyField('PriceHistoryModel')
    link = models.CharField(max_length=1000)
    residence = models.ForeignKey('ResidenceModel', on_delete=models.CASCADE)
    tax = models.ForeignKey('TaxModel', on_delete=models.CASCADE)

    @property
    def price(self):
        # TODO: You will need to implement the property to convert the decimal value price to abbreviated
        pass

    class Meta:
        app_label = "sales"
