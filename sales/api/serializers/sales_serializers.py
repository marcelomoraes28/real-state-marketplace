from django.db import transaction

from sales.api.serializers import BaseSerializer
from sales.models import AreaUnitModel, CityModel, HomeTypeModel, \
    PriceHistoryModel, TaxModel, ResidenceModel, ZRentInformationModel, \
    ZSaleInformationModel, ZillowModel, AnnouncementModel


class AreaUnitSerializer(BaseSerializer):
    class Meta:
        lookup_field = 'uuid'
        model = AreaUnitModel
        fields = ('uuid', 'name')


class CitySerializer(BaseSerializer):
    class Meta:
        lookup_field = 'uuid'
        model = CityModel
        fields = ('uuid', 'name', 'state')


class HomeTypeSerializer(BaseSerializer):
    class Meta:
        lookup_field = 'uuid'
        model = HomeTypeModel
        fields = ('uuid', 'type')


class PriceHistorySerializer(BaseSerializer):
    class Meta:
        model = PriceHistoryModel
        fields = ('uuid', 'sell_price', 'abbreviate_price', 'rent_price',
                  'last_sold_date', 'last_sold_price')


class TaxSerializer(BaseSerializer):
    class Meta:
        model = TaxModel
        fields = ('uuid', 'tax_value', 'tax_year')


class ResidenceSerializer(BaseSerializer):
    city = CitySerializer()
    area_unit = AreaUnitSerializer()
    home_type = HomeTypeSerializer()

    @transaction.atomic
    def create(self, validated_data):
        city_data = validated_data.pop('city')
        area_unit_data = validated_data.pop('area_unit')
        home_type_data = validated_data.pop('home_type')
        city = CityModel.objects.get_or_create(**city_data)[0]
        area_unit = AreaUnitModel.objects.get_or_create(**area_unit_data)[0]
        home_type = HomeTypeModel.objects.get_or_create(**home_type_data)[0]
        residence = ResidenceModel.objects.create(city=city,
                                                  area_unit=area_unit,
                                                  home_type=home_type,
                                                  **validated_data)
        return residence

    class Meta:
        model = ResidenceModel
        lookup_field = 'uuid'
        fields = ('uuid', 'city', 'area_unit', 'address', 'bathrooms',
                  'bedrooms', 'home_size', 'home_type', 'property_size',
                  'year_built')


class ZRentInformationSerializer(BaseSerializer):
    class Meta:
        model = ZRentInformationModel
        fields = ('uuid', 'rentzestimate_amount', 'rentzestimate_last_updated')


class ZSaleInformationSerializer(BaseSerializer):
    class Meta:
        model = ZSaleInformationModel
        fields = ('uuid', 'zestimate_last_updated', 'zestimate_amount')


class ZillowSerializer(BaseSerializer):
    z_rent_information = ZRentInformationSerializer(required=True)
    z_sale_information = ZSaleInformationSerializer(required=True)

    @transaction.atomic
    def create(self, validated_data):
        z_rent_information_data = validated_data.pop('z_rent_information')
        z_sale_information_unit_data = validated_data.pop('z_sale_information')
        z_rent_information = ZRentInformationModel.objects.create(**z_rent_information_data)  # noqa
        z_sale_information = ZSaleInformationModel.objects.create(**z_sale_information_unit_data)  # noqa
        zillow = ZillowModel.objects.create(z_rent_information=z_rent_information,  # noqa
                                            z_sale_information=z_sale_information,  # noqa
                                            **validated_data)
        return zillow

    class Meta:
        model = ZillowModel
        fields = ('uuid', 'zillow_id', 'z_rent_information',
                  'z_sale_information')


class AnnouncementSerializer(BaseSerializer):
    zillow = ZillowSerializer()
    price_history = PriceHistorySerializer(many=True)
    residence = ResidenceSerializer()
    tax = TaxSerializer()

    @transaction.atomic
    def create(self, validated_data):
        zillow_data = validated_data.pop('zillow', None)
        price_history_data = validated_data.pop('price_history', [])
        residence = validated_data.pop('residence', None)
        tax_data = validated_data.pop('tax', None)
        tax = TaxSerializer(data=tax_data)
        residence = ResidenceSerializer(data=residence)
        zillow = ZillowSerializer(data=zillow_data)
        if tax.is_valid() and residence.is_valid() and zillow.is_valid():
            tax.save()
            zillow.save()
            residence.save()
            announcement = AnnouncementModel.objects.create(
                zillow=zillow.instance,
                tax=tax.instance,
                residence=residence.instance,
                **validated_data)

            for p_history in price_history_data:
                price_history = PriceHistoryModel.objects.create(**p_history)
                announcement.price_history.add(price_history)
        return announcement

    class Meta:
        model = AnnouncementModel
        fields = ('uuid', 'zillow', 'price_history',
                  'link', 'residence', 'tax')
