from rest_framework import routers

from sales.api.resources.sales_resources import AreaUnitViewSet, CityViewSet, \
    HomeTypeViewSet, PriceHistoryViewSet, TaxViewSet, ResidenceViewSet, \
    ZRentInformationViewSet, ZSaleInformationViewSet, ZillowViewSet, \
    AnnouncementViewSet

router = routers.DefaultRouter()

router.register(r'area_unit', AreaUnitViewSet)
router.register(r'city', CityViewSet)
router.register(r'home_type', HomeTypeViewSet)
router.register(r'price_history', PriceHistoryViewSet)
router.register(r'tax', TaxViewSet)
router.register(r'residence', ResidenceViewSet)
router.register(r'z_rent_information', ZRentInformationViewSet)
router.register(r'z_sale_information', ZSaleInformationViewSet)
router.register(r'zillow', ZillowViewSet)
router.register(r'announcement', AnnouncementViewSet)
