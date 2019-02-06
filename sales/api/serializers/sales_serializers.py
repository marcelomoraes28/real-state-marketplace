from sales.api.serializers import BaseSerializer
from sales.models import AreaUnitModel, CityModel, HomeTypeModel, \
    PriceHistoryModel, TaxModel, ResidenceModel, ZRentInformationModel, \
    ZSaleInformationModel, ZillowModel, AnnouncementModel


class AreaUnitSerializer(BaseSerializer):
    class Meta:
        model = AreaUnitModel
        fields = ('uuid', 'name')


class CitySerializer(BaseSerializer):
    class Meta:
        model = CityModel
        fields = ('uuid', 'name', 'state')


class HomeTypeSerializer(BaseSerializer):
    class Meta:
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
    city = CitySerializer(read_only=False)
    area_unit = AreaUnitSerializer(read_only=False)

    class Meta:
        model = ResidenceModel
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
    z_rent_information = ZRentInformationSerializer(read_only=False)
    z_sale_information = ZSaleInformationSerializer(read_only=False)

    class Meta:
        model = ZillowModel
        fields = ('uuid', 'zillow_id', 'z_rent_information',
                  'z_sale_information')


class AnnouncementSerializer(BaseSerializer):
    zillow = ZillowSerializer(read_only=False)
    price_history = PriceHistorySerializer(many=True, read_only=False)
    residence = ResidenceSerializer(read_only=False)
    tax = TaxSerializer(read_only=False)

    class Meta:
        model = AnnouncementModel
        fields = ('uuid', 'zillow', 'price_history',
                  'link', 'residence', 'tax')
