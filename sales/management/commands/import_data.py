import csv
from django.core.management import BaseCommand
from django.db import transaction, IntegrityError

from sales.helpers.date import format_date
from sales.helpers.money import abbreviate_to_decimal
from sales.models.file_history import FileHistory
from sales.models.sales_models import AnnouncementModel, ZillowModel, PriceHistoryModel, \
    ResidenceModel, TaxModel, ZRentInformationModel, ZSaleInformationModel, AreaUnitModel, HomeTypeModel, \
    CityModel


class Command(BaseCommand):
    help = 'Insert csv fixture into Database'

    def add_arguments(self, parser):
        parser.add_argument('path_file', type=str)

    @transaction.atomic
    def handle(self, *args, **options):
        path_file = options.get('path_file')
        with open(path_file) as f:
            try:
                FileHistory.create_file_history(path_file=path_file, text=f.read())
                reader = csv.DictReader(f)
                for row in reader:
                    self.stdout.write("Persist data {}".format(str(dict(row))))
                    city = {
                        "name": row.get('city'),
                        "state": row.get('state')
                    }
                    area_unit = {
                        "name": row.get('area_unit'),
                    }
                    home_type = {
                        "type": row.get('home_type')
                    }
                    residence = {
                        "city": CityModel.objects.get_or_create(**city)[0],
                        "area_unit": AreaUnitModel.objects.get_or_create(**area_unit)[0],  # noqa
                        "address": row.get('address'),
                        "bathrooms": row.get('bathrooms') if row.get('bathrooms') else None,  # noqa
                        "bedrooms": row.get('bedrooms'),
                        "home_size": row.get('home_size') if row.get('home_size') else None,  # noqa
                        "home_type": HomeTypeModel.objects.get_or_create(**home_type)[0],  # noqa
                        "property_size": row.get('property_size') if row.get('property_size') else None,  # noqa
                        "year_built": row.get('year_built') if row.get('year_built') else None,  # noqa

                    }
                    price_history = {
                        "sell_price": abbreviate_to_decimal(row.get('price')),
                        "rent_price": float(row.get('rent_price')) if row.get('rent_price') else None,  # noqa
                        "last_sold_date": format_date(row.get('last_sold_date')),
                        "last_sold_price": float(row.get('last_sold_price')) if row.get('last_sold_price') else None,  # noqa
                    }
                    z_sale_information = {
                        "zestimate_last_updated": format_date(row.get('zestimate_last_updated')),  # noqa
                        "zestimate_amount": float(row.get('zestimate_amount')) if row.get('zestimate_amount') else None,  # noqa
                    }
                    z_rent_information = {
                        "rentzestimate_amount": float(row.get('rentzestimate_amount')) if row.get('rentzestimate_amount') else None,  # noqa
                        "rentzestimate_last_updated": format_date(row.get('rentzestimate_last_updated')),  # noqa
                    }
                    tax = {
                        "tax_value": float(row.get('tax_value')),
                        "tax_year": row.get('tax_year')
                    }

                    zillow = {
                        "zillow_id": int(row.get('zillow_id')),
                        "z_rent_information": ZRentInformationModel.objects.get_or_create(**z_rent_information)[0],  # noqa
                        "z_sale_information": ZSaleInformationModel.objects.get_or_create(**z_sale_information)[0],  # noqa
                    }
                    zillow = ZillowModel.objects.get_or_create(**zillow)[0]

                    residence = ResidenceModel.objects.get_or_create(**residence)[0]  # noqa
                    tax = TaxModel.objects.get_or_create(**tax)[0]
                    price_history = PriceHistoryModel.objects.get_or_create(**price_history)[0]
                    announcement = AnnouncementModel.objects.get_or_create(link=row.get('link'),
                                                                           zillow=zillow,
                                                                           residence=residence,
                                                                           tax=tax)[0]  # noqa
                    announcement.price_history.add(price_history)
            except IntegrityError:
                self.stdout.write("This file has already been imported")
