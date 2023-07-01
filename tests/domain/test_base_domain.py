from faker import Faker
from src.domain.base_domain import BaseDomain
from src.domain.user import User
from src.utils.requests import InvalidResquest, ValidRequest

fake = Faker()


def test_from_dict():
    instance = BaseDomain.from_dict({})

    assert isinstance(instance, BaseDomain)


def test_to_dict():
    dict_object = BaseDomain().to_dict()

    assert dict_object == {}
    assert isinstance(dict_object, dict)


def test_get_error_as_dict():
    instance = BaseDomain()
    expected_error = {
        "parameter": "Exception",
        "message": "Some Exception error",
    }

    instance._errors.append(Exception("Some Exception error"))
    dict_error = instance.get_error_as_dict(0)

    assert dict_error == expected_error


def test_add_error():
    error_message = fake.word()
    instance = BaseDomain()

    instance._errors.append(ValueError(error_message))
    error = instance._errors[0]

    assert str(error) == error_message
    assert isinstance(error, ValueError)


class TestHasErrors:
    def test_with_errors(self):
        instance = BaseDomain()
        instance._errors.append(ValueError(fake.word()))

        assert instance.has_errors() is True

    def test_without_error(self):
        instance = BaseDomain()

        assert instance.has_errors() is False


def test_any_with_errors(mocker):
    instance = BaseDomain()
    instance._errors = [ValueError(fake.word())]

    request = instance.get_request()

    assert isinstance(request, InvalidResquest)


def test_any_without_errors(mocker):
    instance = BaseDomain()

    request = instance.get_request()

    assert isinstance(request, ValidRequest)
