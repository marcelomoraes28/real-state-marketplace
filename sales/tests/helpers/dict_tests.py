import pytest
from django.test import TestCase

from sales.helpers.dict_ import count_dict
from sales.helpers.exceptions import Dict_Exception


class Dict_Test(TestCase):
    def test_dict__one_level(self):
        payload = {"name": "Marcelo",
                   "city": "Curitiba"}
        assert count_dict(payload) == 1

    def test_dict__two_level(self):
        payload = {"name": "Marcelo",
                   "city": "Curitiba",
                   "family": {"name": "Moraes"}
                   }
        assert count_dict(payload) == 2

    def test_dict__tree_level(self):
        payload = {"name": "Marcelo",
                   "city": "Curitiba",
                   "family": {"name": "Moraes",
                              "foo": {"foo": "bar"}
                              }
                   }
        assert count_dict(payload) == 3

    def test_dict__invalid_dict(self):
        payload = "foo-bar"
        with pytest.raises(Dict_Exception):
            count_dict(payload)
