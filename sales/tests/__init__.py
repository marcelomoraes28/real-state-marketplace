from django.test import TestCase

from sales.models import AreaUnitModel, CityModel, HomeTypeModel, \
    PriceHistoryModel, TaxModel, ResidenceModel, ZRentInformationModel, \
    ZSaleInformationModel, ZillowModel, AnnouncementModel


class BaseTestCase(TestCase):
    def setUp(self):
        self.import_data_payload = {'area_unit': 'SqFt', 'bathrooms': '2.0', 'bedrooms': '4',
                                    'home_size': '1372', 'home_type': 'SingleFamily',
                                    'last_sold_date': '', 'last_sold_price': '',
                                    'link': 'https://www.zillow.com/homedetails/7417-Quimby-Ave-West-Hills-CA-91307/19866015_zpid/',
                                    'price': '$739K', 'property_size': '10611',
                                    'rent_price': '', 'rentzestimate_amount': '2850',
                                    'rentzestimate_last_updated': '08/07/2018',
                                    'tax_value': '215083.0', 'tax_year': '2017',
                                    'year_built': '1956', 'zestimate_amount': '709630',
                                    'zestimate_last_updated': '08/07/2018',
                                    'zillow_id': '19866015', 'address': '7417 Quimby Ave',
                                    'city': 'West Hills', 'state': 'CA', 'zipcode': '91307'}

        self.area_unit = AreaUnitModel.objects.create(name='Area 51')
        self.city = CityModel.objects.create(name='Curitiba', state='Parana')
        self.home_type = HomeTypeModel.objects.create(type='Apartment')
        self.price_history = PriceHistoryModel.objects.create(sell_price=1000000.00,
                                                         rent_price=1000.00)
        self.tax = TaxModel.objects.create(tax_value=1240.00, tax_year=1992)
        self.residene = ResidenceModel.objects.create(city=self.city,
                                                 area_unit=self.area_unit,
                                                 address='R. Lothario Boutin 220',
                                                 bathrooms=2.5,
                                                 bedrooms=2,
                                                 home_size=124,
                                                 home_type=self.home_type,
                                                 property_size=200,
                                                 year_built=1994)

        self.z_rent_information = ZRentInformationModel.objects.create(rentzestimate_amount=100012.00)
        self.z_sale_information = ZSaleInformationModel.objects.create(zestimate_amount=99123.31)
        self.zillow = ZillowModel.objects.create(zillow_id=123,
                                                 z_rent_information=self.z_rent_information,
                                                 z_sale_information=self.z_sale_information)
        self.announcement = AnnouncementModel.objects.create(
            zillow=self.zillow,
            link='localhost:8000',
            residence=self.residene,
            tax=self.tax
        )
        self.announcement.price_history.add(self.price_history)
