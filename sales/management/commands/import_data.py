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
                    AnnouncementModel.import_data(row)
            except IntegrityError:
                self.stdout.write("This file has already been imported")
