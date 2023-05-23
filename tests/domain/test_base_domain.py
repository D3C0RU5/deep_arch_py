from faker import Faker
from src.domain.base_domain import BaseDomain

fake = Faker()


def test_from_dict():
    instance = BaseDomain.from_dict({})

    assert isinstance(instance, BaseDomain)


def test_to_dict():
    dict_object = BaseDomain().to_dict()

    assert dict_object == {}
    assert isinstance(dict_object, dict)
