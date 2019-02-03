import pytest
from django.test import TestCase

from sales.helpers.exceptions import HMoneyException
from sales.helpers.money import abbreviate_to_decimal


class MoneyTest(TestCase):
    def test_abbreviate_to_decimal_invalid_value(self):
        with pytest.raises(HMoneyException):
            abbreviate_to_decimal('%124.12K')

    def test_abbreviate_to_decimal_k(self):
        assert abbreviate_to_decimal('$739K') == 739000.0
        assert abbreviate_to_decimal('$23K') == 23000.0
        assert abbreviate_to_decimal('$3K') == 3000.0

    def test_abbreviate_to_decimal_m(self):
        assert abbreviate_to_decimal('$739M') == 739000000.0
        assert abbreviate_to_decimal('$23M') == 23000000.0
        assert abbreviate_to_decimal('$3M') == 3000000.0

    def test_abbreviate_to_decimal_b(self):
        assert abbreviate_to_decimal('$739B') == 739000000000.0
        assert abbreviate_to_decimal('$23B') == 23000000000.0
        assert abbreviate_to_decimal('$3B') == 3000000000.0

    def test_abbreviate_to_decimal_m_with_dot(self):
        assert abbreviate_to_decimal('$233.7M') == 233700000.0
        assert abbreviate_to_decimal('$73.9M') == 73900000.0
        assert abbreviate_to_decimal('$2.3M') == 2300000.0

    def test_abbreviate_to_decimal_b_with_dot(self):
        assert abbreviate_to_decimal('$739.6B') == 739600000000.0
        assert abbreviate_to_decimal('$23.3B') == 23300000000.0
        assert abbreviate_to_decimal('$3.2B') == 3200000000.0
