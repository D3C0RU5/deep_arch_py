from pydantic import ValidationError
import pytest
from app.core.entities.user import UserEntity


def test_user_create(faker):
    fake_name = faker.word()
    fake_email = faker.email()
    fake_password = faker.password()

    user = UserEntity(
        name=fake_name,
        email=fake_email,
        password=fake_password,
    )

    assert user.name == fake_name
    assert user.email == fake_email
    assert user.password == fake_password


def test_user_create_throws_invalid_name(user_factory):
    with pytest.raises(ValidationError) as exc:
        user_factory(name={})

    assert exc.value.errors()[0]["loc"][0] == "name"
    assert exc.value.errors()[0]["msg"] == "str type expected"


def test_user_create_throws_invalid_password(user_factory):
    with pytest.raises(ValidationError, match="") as exc:
        user_factory(password={})

    assert exc.value.errors()[0]["loc"][0] == "password"
    assert exc.value.errors()[0]["msg"] == "str type expected"
