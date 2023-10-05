import factory
import pytest

from app.core.entities.user import UserEntity


class UserFactory(factory.Factory):
    class Meta:
        model = UserEntity

    id = factory.Faker("random_int")
    name = factory.Faker("word")
    email = factory.Faker("email")
    password = factory.Faker("password")


@pytest.fixture
def user_factory():
    return UserFactory
