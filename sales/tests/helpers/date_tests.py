from datetime import datetime

import pytest
from django.test import TestCase

from sales.helpers.date import format_date
from sales.helpers.exceptions import HDateException


class DateTest(TestCase):
    def test_format_date_invalid_input_pattern(self):
        dt = '02/03/2019'
        with pytest.raises(HDateException):
            format_date(date=dt, input_pattern='foo-bar')

    def test_format_date_invalid_output_pattern(self):
        dt = '02/03/2019'
        assert 'foo-bar' == format_date(date=dt, output_pattern='foo-bar')

    def test_format_date_invalid_date(self):
        dt = 'foo-bar'
        with pytest.raises(HDateException):
            format_date(date=dt)

    def test_format_date_valid_date(self):
        dt = '02/03/2019'
        assert format_date(date=dt) == '2019-02-03'

    def test_format_date_change_output_format(self):
        dt = '02/03/2019'
        assert format_date(date=dt, output_pattern='%d-%m-%Y') == '03-02-2019'

    def test_format_date_change_input_and_output_format(self):
        dt = '2019-02-03'
        assert format_date(date=dt, input_pattern='%Y-%m-%d',
                           output_pattern='%d/%m/%Y') == '03/02/2019'

    def test_format_date_obj_return(self):
        dt = '02/03/2019'
        assert isinstance(format_date(date=dt, string=False), datetime)
