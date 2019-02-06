from sales.api.resources import BaseViewSet
from sales.api.serializers.sales_serializers import AreaUnitSerializer, \
    CitySerializer, HomeTypeSerializer, PriceHistorySerializer, TaxSerializer, \
    ResidenceSerializer, ZRentInformationSerializer, \
    ZSaleInformationSerializer, ZillowSerializer, AnnouncementSerializer
from sales.models import AreaUnitModel, CityModel, HomeTypeModel, \
    PriceHistoryModel, TaxModel, ResidenceModel, ZRentInformationModel, \
    ZSaleInformationModel, ZillowModel, AnnouncementModel


class AreaUnitViewSet(BaseViewSet):
    """
    API endpoint AreaUnitViewSet
    """
    queryset = AreaUnitModel.objects.all()
    serializer_class = AreaUnitSerializer


class CityViewSet(BaseViewSet):
    """
    API endpoint AreaUnitViewSet
    """
    queryset = CityModel.objects.all()
    serializer_class = CitySerializer


class HomeTypeViewSet(BaseViewSet):
    """
    API endpoint AreaUnitViewSet
    """
    queryset = HomeTypeModel.objects.all()
    serializer_class = HomeTypeSerializer


class PriceHistoryViewSet(BaseViewSet):
    """
    API endpoint AreaUnitViewSet
    """
    queryset = PriceHistoryModel.objects.all()
    serializer_class = PriceHistorySerializer


class TaxViewSet(BaseViewSet):
    """
    API endpoint AreaUnitViewSet
    """
    queryset = TaxModel.objects.all()
    serializer_class = TaxSerializer


class ResidenceViewSet(BaseViewSet):
    """
    API endpoint AreaUnitViewSet
    """
    queryset = ResidenceModel.objects.all()
    serializer_class = ResidenceSerializer


class ZRentInformationViewSet(BaseViewSet):
    """
    API endpoint AreaUnitViewSet
    """
    queryset = ZRentInformationModel.objects.all()
    serializer_class = ZRentInformationSerializer


class ZSaleInformationViewSet(BaseViewSet):
    """
    API endpoint AreaUnitViewSet
    """
    queryset = ZSaleInformationModel.objects.all()
    serializer_class = ZSaleInformationSerializer


class ZillowViewSet(BaseViewSet):
    """
    API endpoint AreaUnitViewSet
    """
    queryset = ZillowModel.objects.all()
    serializer_class = ZillowSerializer


class AnnouncementViewSet(BaseViewSet):
    """
    API endpoint AreaUnitViewSet
    """
    queryset = AnnouncementModel.objects.all()
    serializer_class = AnnouncementSerializer
