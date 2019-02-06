from rest_framework import routers

from sales.api.resources.sales_resources import AreaUnitViewSet, CityViewSet, \
    HomeTypeViewSet, PriceHistoryViewSet, TaxViewSet, ResidenceViewSet, \
    ZRentInformationViewSet, ZSaleInformationViewSet, ZillowViewSet, \
    AnnouncementViewSet

router = routers.DefaultRouter()

router.register(r'areaUnit', AreaUnitViewSet)
router.register(r'city', CityViewSet)
router.register(r'homeType', HomeTypeViewSet)
router.register(r'priceHistory', PriceHistoryViewSet)
router.register(r'tax', TaxViewSet)
router.register(r'residence', ResidenceViewSet)
router.register(r'zRentInformation', ZRentInformationViewSet)
router.register(r'zSaleInformation', ZSaleInformationViewSet)
router.register(r'zillow', ZillowViewSet)
router.register(r'announcement', AnnouncementViewSet)
