from copy import deepcopy

import pytest
from django.db import IntegrityError

from sales.models import AnnouncementModel
from sales.tests import BaseTestCase


class AnnouncementTest(BaseTestCase):
    def test_import_data_valid_payload(self):

        data = AnnouncementModel.import_data(self.import_data_payload)
        assert isinstance(data, object)

    def test_import_data_invalid_payload(self):
        payload = deepcopy(self.import_data_payload)
        del payload['city']
        with pytest.raises(IntegrityError):
            AnnouncementModel.import_data(payload)

