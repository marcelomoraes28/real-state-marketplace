from rest_framework.test import APIClient
from rest_framework import status

from sales.models import AreaUnitModel, CityModel, HomeTypeModel, \
    PriceHistoryModel, TaxModel, ResidenceModel, ZRentInformationModel, \
    ZSaleInformationModel, ZillowModel, AnnouncementModel
from sales.tests import BaseTestCase


class AreaUnitTest(BaseTestCase):
    def test_retrieve(self):
        factory = APIClient()
        unit_area = AreaUnitModel.objects.first()
        req = factory.get(f'/sales/api/area_unit/{unit_area.uuid}/')
        assert req.status_code == status.HTTP_200_OK
        assert req.json()['uuid'] == str(unit_area.uuid)

    def test_update(self):
        factory = APIClient()
        unit_area = AreaUnitModel.objects.first()
        req = factory.patch(f'/sales/api/area_unit/{unit_area.uuid}/',
                            data={"name": "Area 52"})
        unit_area = AreaUnitModel.objects.first()
        assert req.status_code == status.HTTP_200_OK
        assert unit_area.name == req.json()['name']

    def test_insert(self):
        factory = APIClient()
        req = factory.post('/sales/api/area_unit/',
                           data={"name": "Area 53"})
        assert req.status_code == status.HTTP_201_CREATED

        assert req.json()['name'] == 'Area 53'

    def test_list(self):
        factory = APIClient()
        req = factory.get('/sales/api/area_unit/')

        assert req.status_code == status.HTTP_200_OK
        assert len(req.json()['results']) == 1

    def test_delete(self):
        del_area = AreaUnitModel.objects.create(name='Del Area')
        factory = APIClient()
        req = factory.delete(f'/sales/api/area_unit/{del_area.uuid}/')
        assert status.HTTP_204_NO_CONTENT == req.status_code


class CityTest(BaseTestCase):
    def test_retrieve(self):
        factory = APIClient()
        city = CityModel.objects.first()
        req = factory.get(f'/sales/api/city/{city.uuid}/')
        assert req.status_code == status.HTTP_200_OK
        assert req.json()['uuid'] == str(city.uuid)

    def test_update(self):
        factory = APIClient()
        city = CityModel.objects.first()
        req = factory.patch(f'/sales/api/city/{city.uuid}/',
                            data={"name": "Kitchener"})
        city = CityModel.objects.first()
        assert req.status_code == status.HTTP_200_OK
        assert city.name == req.json()['name']

    def test_insert(self):
        factory = APIClient()
        req = factory.post('/sales/api/city/',
                           data={"name": "Kitchener",
                                 "state": "ON"})
        assert req.status_code == status.HTTP_201_CREATED

        assert req.json()['name'] == 'Kitchener'

    def test_list(self):
        factory = APIClient()
        req = factory.get('/sales/api/city/')

        assert req.status_code == status.HTTP_200_OK
        assert len(req.json()['results']) == 1

    def test_delete(self):
        del_city = CityModel.objects.create(name='Kitchener', state='ON')
        factory = APIClient()
        req = factory.delete(f'/sales/api/city/{del_city.uuid}/')
        assert status.HTTP_204_NO_CONTENT == req.status_code


class HomeTypeTest(BaseTestCase):
    def test_retrieve(self):
        factory = APIClient()
        home_type = HomeTypeModel.objects.first()
        req = factory.get(f'/sales/api/home_type/{home_type.uuid}/')
        assert req.status_code == status.HTTP_200_OK
        assert req.json()['uuid'] == str(home_type.uuid)

    def test_update(self):
        factory = APIClient()
        home_type = HomeTypeModel.objects.first()
        req = factory.patch(f'/sales/api/home_type/{home_type.uuid}/',
                            data={"type": "House"})
        home_type = HomeTypeModel.objects.first()
        assert req.status_code == status.HTTP_200_OK
        assert home_type.type == req.json()['type']

    def test_insert(self):
        factory = APIClient()
        req = factory.post('/sales/api/home_type/',
                           data={"type": "House"})
        assert req.status_code == status.HTTP_201_CREATED

        assert req.json()['type'] == 'House'

    def test_list(self):
        factory = APIClient()
        req = factory.get('/sales/api/home_type/')

        assert req.status_code == status.HTTP_200_OK
        assert len(req.json()['results']) == 1

    def test_delete(self):
        del_home_type = HomeTypeModel.objects.create(type='House')
        factory = APIClient()
        req = factory.delete(f'/sales/api/home_type/{del_home_type.uuid}/')
        assert status.HTTP_204_NO_CONTENT == req.status_code


class PriceHistoryTest(BaseTestCase):
    def test_retrieve(self):
        factory = APIClient()
        price_history = PriceHistoryModel.objects.first()
        req = factory.get(f'/sales/api/price_history/{price_history.uuid}/')
        assert req.status_code == status.HTTP_200_OK
        assert req.json()['uuid'] == str(price_history.uuid)

    def test_update(self):
        factory = APIClient()
        price_history = PriceHistoryModel.objects.first()
        req = factory.patch(f'/sales/api/price_history/{price_history.uuid}/',
                            data={
                                "last_sold_price": 8000.0,
                                "last_sold_date": "2018-10-10"
                            },
                            format='json')
        price_history = PriceHistoryModel.objects.first()
        assert req.status_code == status.HTTP_200_OK
        assert str(price_history.last_sold_date) == req.json()['last_sold_date']
        assert str(price_history.last_sold_price) == req.json()['last_sold_price']

    def test_insert(self):
        factory = APIClient()
        req = factory.post('/sales/api/price_history/',
                           data={"sell_price": 750000.00,
                                 "rent_price": 750.00})
        assert req.status_code == status.HTTP_201_CREATED

        assert req.json()['sell_price'] == '750000.00'

    def test_list(self):
        factory = APIClient()
        req = factory.get('/sales/api/price_history/')

        assert req.status_code == status.HTTP_200_OK
        assert len(req.json()['results']) == 1

    def test_delete(self):
        del_price_history = PriceHistoryModel.objects.create(
            **{"sell_price": 750000.00,
               "rent_price": 750.00})
        factory = APIClient()
        req = factory.delete(
            f'/sales/api/price_history/{del_price_history.uuid}/')
        assert status.HTTP_204_NO_CONTENT == req.status_code


class TaxTest(BaseTestCase):
    def test_retrieve(self):
        factory = APIClient()
        tax = TaxModel.objects.first()
        req = factory.get(f'/sales/api/tax/{tax.uuid}/')
        assert req.status_code == status.HTTP_200_OK
        assert req.json()['uuid'] == str(tax.uuid)

    def test_update(self):
        factory = APIClient()
        tax = TaxModel.objects.first()
        req = factory.patch(f'/sales/api/tax/{tax.uuid}/',
                            data={"tax_year": 2019,
                                  "tax_value": 800.00})
        tax = TaxModel.objects.first()
        assert req.status_code == status.HTTP_200_OK
        assert tax.tax_year == req.json()['tax_year']
        assert str(tax.tax_value) == req.json()['tax_value']

    def test_insert(self):
        factory = APIClient()
        req = factory.post('/sales/api/tax/',
                           data={"tax_year": 2019,
                                 "tax_value": 800.00})
        assert req.status_code == status.HTTP_201_CREATED

        assert req.json()['tax_year'] == 2019
        assert req.json()['tax_value'] == '800.00'

    def test_list(self):
        factory = APIClient()
        req = factory.get('/sales/api/tax/')

        assert req.status_code == status.HTTP_200_OK
        assert len(req.json()['results']) == 1

    def test_delete(self):
        del_tax = TaxModel.objects.create(**{"tax_year": 2019,
                                             "tax_value": 800.00})
        factory = APIClient()
        req = factory.delete(f'/sales/api/tax/{del_tax.uuid}/')
        assert status.HTTP_204_NO_CONTENT == req.status_code


class ResidenceTest(BaseTestCase):
    def test_retrieve(self):
        factory = APIClient()
        residence = ResidenceModel.objects.first()
        req = factory.get(f'/sales/api/residence/{residence.uuid}/')
        assert req.status_code == status.HTTP_200_OK
        assert req.json()['uuid'] == str(residence.uuid)

    def test_update(self):
        factory = APIClient()
        residence = ResidenceModel.objects.first()
        req = factory.patch(f'/sales/api/residence/{residence.uuid}/',
                            data={"year_built": 1990,
                                  "home_size": 100,
                                  "city": {"name": "Toronto"}},
                            format='json')
        residence = ResidenceModel.objects.first()
        assert req.status_code == status.HTTP_200_OK
        assert residence.year_built == req.json()['year_built']
        assert residence.home_size == req.json()['home_size']
        assert residence.city.name == req.json()['city']['name']

    def test_insert(self):
        factory = APIClient()
        req = factory.post('/sales/api/residence/',
                           data={"city": {"name": "Toronto",
                                          "state": "ON"},
                                 "area_unit": {"name": "Area 53"},
                                 "address": "Spadina",
                                 "bathrooms": 2.5,
                                 "bedrooms": 2,
                                 "home_size": 60,
                                 "home_type": {"type": "House"},
                                 "property_size": 80,
                                 "year_built": 2000},
                           format='json')

        assert req.status_code == status.HTTP_201_CREATED
        assert req.json()['year_built'] == 2000
        assert req.json()['property_size'] == 80
        assert req.json()['address'] == "Spadina"

    def test_list(self):
        factory = APIClient()
        req = factory.get('/sales/api/residence/')

        assert req.status_code == status.HTTP_200_OK
        assert len(req.json()['results']) == 1

    def test_delete(self):
        del_residence = ResidenceModel.objects.first()
        factory = APIClient()
        req = factory.delete(f'/sales/api/residence/{del_residence.uuid}/')
        assert status.HTTP_204_NO_CONTENT == req.status_code


class ZRentInformationTest(BaseTestCase):
    def test_retrieve(self):
        factory = APIClient()
        z_rent_information = ZRentInformationModel.objects.first()
        req = factory.get(f'/sales/api/z_rent_information/{z_rent_information.uuid}/')
        assert req.status_code == status.HTTP_200_OK
        assert req.json()['uuid'] == str(z_rent_information.uuid)

    def test_update(self):
        factory = APIClient()
        z_rent_information = ZRentInformationModel.objects.first()
        req = factory.patch(f'/sales/api/z_rent_information/{z_rent_information.uuid}/',
                            data={"rentzestimate_amount": 999.00})
        z_rent_information = ZRentInformationModel.objects.first()
        assert req.status_code == status.HTTP_200_OK
        assert str(z_rent_information.rentzestimate_amount) == req.json()['rentzestimate_amount']

    def test_insert(self):
        factory = APIClient()
        req = factory.post('/sales/api/z_rent_information/',
                           data={"rentzestimate_amount": 12345.12})
        assert req.status_code == status.HTTP_201_CREATED

        assert req.json()['rentzestimate_amount'] == '12345.12'

    def test_list(self):
        factory = APIClient()
        req = factory.get('/sales/api/z_rent_information/')

        assert req.status_code == status.HTTP_200_OK
        assert len(req.json()['results']) == 1

    def test_delete(self):
        del_z_rent_information = ZRentInformationModel.objects.create(rentzestimate_amount=123.12)
        factory = APIClient()
        req = factory.delete(f'/sales/api/z_rent_information/{del_z_rent_information.uuid}/')
        assert status.HTTP_204_NO_CONTENT == req.status_code


class ZSaleInformationTest(BaseTestCase):
    def test_retrieve(self):
        factory = APIClient()
        z_sale_information = ZSaleInformationModel.objects.first()
        req = factory.get(f'/sales/api/z_sale_information/{z_sale_information.uuid}/')
        assert req.status_code == status.HTTP_200_OK
        assert req.json()['uuid'] == str(z_sale_information.uuid)

    def test_update(self):
        factory = APIClient()
        z_sale_information = ZSaleInformationModel.objects.first()
        req = factory.patch(f'/sales/api/z_sale_information/{z_sale_information.uuid}/',
                            data={"zestimate_amount": 999.00})
        z_sale_information = ZSaleInformationModel.objects.first()
        assert req.status_code == status.HTTP_200_OK
        assert str(z_sale_information.zestimate_amount) == req.json()['zestimate_amount']

    def test_insert(self):
        factory = APIClient()
        req = factory.post('/sales/api/z_sale_information/',
                           data={"zestimate_amount": 12345.12})
        assert req.status_code == status.HTTP_201_CREATED

        assert req.json()['zestimate_amount'] == '12345.12'

    def test_list(self):
        factory = APIClient()
        req = factory.get('/sales/api/z_sale_information/')

        assert req.status_code == status.HTTP_200_OK
        assert len(req.json()['results']) == 1

    def test_delete(self):
        del_z_sale_information = ZSaleInformationModel.objects.create(zestimate_amount=123.12)
        factory = APIClient()
        req = factory.delete(f'/sales/api/z_sale_information/{del_z_sale_information.uuid}/')
        assert status.HTTP_204_NO_CONTENT == req.status_code


class ZillowTest(BaseTestCase):
    def test_retrieve(self):
        factory = APIClient()
        zillow = ZillowModel.objects.first()
        req = factory.get(f'/sales/api/zillow/{zillow.uuid}/')
        assert req.status_code == status.HTTP_200_OK
        assert req.json()['uuid'] == str(zillow.uuid)

    def test_update(self):
        factory = APIClient()
        zillow = ZillowModel.objects.first()
        req = factory.patch(f'/sales/api/zillow/{zillow.uuid}/',
                            data={"zillow_id": 1,
                                  "z_rent_information":
                                      {"rentzestimate_amount": 12.12},
                                  "z_sale_information":
                                      {"zestimate_amount": 10}  # noqa
                                  }, format='json')
        zillow = ZillowModel.objects.first()

        assert req.status_code == status.HTTP_200_OK
        assert zillow.zillow_id == req.json()['zillow_id']
        assert str(zillow.z_rent_information.rentzestimate_amount) == req.json()['z_rent_information']['rentzestimate_amount']  # noqa
        assert str(zillow.z_sale_information.zestimate_amount) == req.json()['z_sale_information']['zestimate_amount']  # noqa

    def test_insert(self):
        factory = APIClient()
        req = factory.post('/sales/api/zillow/',
                           data={"zillow_id": 5,
                                 "z_rent_information":
                                     {"rentzestimate_amount": 4144.11},
                                 "z_sale_information":
                                     {"zestimate_amount": 0.0}  # noqa
                                 },
                           format='json')
        assert req.status_code == status.HTTP_201_CREATED
        assert req.json()['z_rent_information']['rentzestimate_amount'] == str(4144.11)  # noqa
        assert req.json()['z_sale_information']['zestimate_amount'] == '0.00'  # noqa
        assert req.json()['zillow_id'] == 5

    def test_list(self):
        factory = APIClient()
        req = factory.get('/sales/api/zillow/')

        assert req.status_code == status.HTTP_200_OK
        assert len(req.json()['results']) == 1

    def test_delete(self):
        del_zillow = ZillowModel.objects.first()
        factory = APIClient()
        req = factory.delete(f'/sales/api/zillow/{del_zillow.uuid}/')
        assert status.HTTP_204_NO_CONTENT == req.status_code


class AnnouncementTest(BaseTestCase):
    def test_retrieve(self):
        factory = APIClient()
        announcement = AnnouncementModel.objects.first()
        req = factory.get(f'/sales/api/announcement/{announcement.uuid}/')
        assert req.status_code == status.HTTP_200_OK
        assert req.json()['uuid'] == str(announcement.uuid)

    def test_update(self):
        factory = APIClient()
        announcement = AnnouncementModel.objects.first()
        req = factory.patch(f'/sales/api/announcement/{announcement.uuid}/',
                            data={"link": 'https://orkut.com',
                                  "zillow": {
                                      "z_rent_information":
                                          {"rentzestimate_amount": 12.12},
                                      "z_sale_information":
                                          {"zestimate_amount": 10}
                                  },
                                  "residence": {"city":
                                      {
                                          "name": "Altonia",
                                          "state": "PR"
                                      }
                                  },
                                  "price_history": [{"sell_price": 1242.00,
                                                     "uuid": announcement.price_history.first().uuid
                                                     }]
                                  }, format='json')
        announcement = AnnouncementModel.objects.first()

        assert req.status_code == status.HTTP_200_OK
        assert announcement.link == req.json()['link']
        assert announcement.residence.city.name == req.json()['residence']['city']['name']
        assert announcement.residence.city.state == req.json()['residence']['city']['state']
        assert str(announcement.zillow.z_sale_information.zestimate_amount) == req.json()['zillow']['z_sale_information']['zestimate_amount']  # noqa
        assert str(announcement.zillow.z_rent_information.rentzestimate_amount) == req.json()['zillow']['z_rent_information']['rentzestimate_amount']  # noqa

    def test_insert(self):
        factory = APIClient()
        req = factory.post('/sales/api/announcement/',
                           data={"link": "https://orkut.com",
                                 "zillow": {
                                     "zillow_id": 5,
                                     "z_rent_information":
                                         {"rentzestimate_amount": 4144.11},
                                     "z_sale_information":
                                         {"zestimate_amount": 0.0}
                                 },
                                 "tax": {"tax_value": 1234.00,
                                         "tax_year": 2019},
                                 "residence": {
                                     "city": {"name": "Vancouver",
                                              "state": "BC"},
                                     "area_unit": {"name": "Unit1"},
                                     "home_type": {"type": "Hotel"},
                                     "address": "R Desembargador Motta",
                                     "bathrooms": 2.5,
                                     "bedrooms": 4,
                                     "home_size": 70,
                                     "property_size": 80,
                                     "year_built": 1997
                                 },
                                 "price_history": [{"sell_price": 1230000.00
                                                    }]
                                 },
                           format='json')
        assert req.status_code == status.HTTP_201_CREATED
        assert req.json()['zillow']['z_rent_information']['rentzestimate_amount'] == '4144.11'
        assert req.json()['zillow']['z_sale_information']['zestimate_amount'] == '0.00'
        assert len(req.json()['price_history']) == 1

    def test_list(self):
        factory = APIClient()
        req = factory.get('/sales/api/announcement/')

        assert req.status_code == status.HTTP_200_OK
        assert len(req.json()['results']) == 1

    def test_delete(self):
        del_announcement = AnnouncementModel.objects.first()
        factory = APIClient()
        req = factory.delete(f'/sales/api/announcement/{del_announcement.uuid}/')
        assert status.HTTP_204_NO_CONTENT == req.status_code
