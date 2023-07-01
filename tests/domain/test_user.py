import uuid
from faker import Faker
import pytest
from src.domain.user import User

fake = Faker()
print()


def test_from_dict():
    user = {
        "name": fake.name(),
        "login": fake.name(),
        "password": fake.password(),
        "email": fake.email(),
    }

    instance = User.from_dict(user)

    assert instance.name == user["name"]
    assert instance.login == user["login"]
    assert instance.password == user["password"]
    assert instance.email == user["email"]
    assert isinstance(instance, User)


def test_to_dict():
    user = User(
        name=fake.name(),
        login=fake.name(),
        password=fake.password(),
        email=fake.email(),
    )

    result = User.to_dict(user)

    assert isinstance(result, dict)
    assert result["name"] == user.name
    assert result["login"] == user.login
    assert result["password"] == user.password
    assert result["email"] == user.email


class TestValidateCode:
    class TestSuccess:
        def test_when_code_is_valid_UUID(self):
            _uuid = uuid.uuid4()
            user = User(code=_uuid)

            assert user.code == _uuid

        def test_when_code_is_valid_str_UUID(self):
            _uuid = "502ab67e-0b06-4395-b4cb-74d248d986a0"
            user = User(code=_uuid)

            assert str(user.code) == _uuid

    class TestFailure:
        @pytest.mark.parametrize(
            "invalid_code", ["502ab67e-0b06-4395-b4cb", "", "any_value"]
        )
        def test_when_code_is_string_but_invalid_uuid(self, invalid_code):
            user = User(code=invalid_code)
            assert user.get_error_as_dict(0) == {
                "parameter": "ValueError",
                "message": "Badly formed hexadecimal UUID string",
            }

        @pytest.mark.parametrize("invalid_code", [11, [], {}, ()])
        def test_when_code_is_not_str_and_invalid_UUID(self, invalid_code):
            with pytest.raises(TypeError, match="Code must be an UUID"):
                User(code=invalid_code)


class TestValidateName:
    class TestSuccess:
        @pytest.mark.parametrize(
            "name",
            ["Some name", "name", "Some other name"],
        )
        def test_valid_name(self, name):
            user = User()
            user.name = name

            try:
                user._User__validate_name()
            except Exception as exc:
                assert False, f"'validate_name' raised an exception {exc}"

    class TestFailure:
        @pytest.mark.parametrize("name", [11, {}, ()])
        def test_invalid_name(self, name):
            user = User()
            user.name = name

            with pytest.raises(TypeError, match="Name must be a string") as exc:
                user._User__validate_name()


class TestValidateLogin:
    class TestSuccess:
        @pytest.mark.parametrize(
            "login",
            ["Some login", "Some other"],
        )
        def test_valid_login(self, login):
            user = User()
            user.login = login

            try:
                user._User__validate_login()
            except Exception as exc:
                assert False, f"'validate_login' raised an exception {exc}"

    class TestFailure:
        @pytest.mark.parametrize(
            "login",
            [11, {}, ()],
        )
        def test_invalid_name(self, login):
            user = User()
            user.login = login

            with pytest.raises(TypeError, match="Login must be a string"):
                user._User__validate_login()


class TestPassword:
    class TestSuccess:
        @pytest.mark.parametrize("password", ["Abcd1234", "1Abcdefghijkl", "123456aA"])
        def test_when_password_is_valid(self, password):
            user = User()
            user.password = password

            try:
                user._User__validate_password()
            except Exception as exc:
                assert False, f"'validate_password' raised an exception {exc}"

    class TestFailure:
        @pytest.mark.parametrize("password", [1, {}, [], (), 123, {"a:1"}, [1], (2, 1)])
        def test_when_is_not_string(self, password):
            user = User()
            user.password = password

            with pytest.raises(TypeError, match="Password must be a string"):
                user._User__validate_password()

        @pytest.mark.parametrize("password", ["a", "1", "acbcd3A"])
        def test_when_has_length_less_than_eight(self, password):
            user = User()
            user.password = password

            with pytest.raises(ValueError, match="Invalid password."):
                user._User__validate_password()

        @pytest.mark.parametrize(
            "password",
            ["abcdefghijklmno", "12345678", "ABCDEFGHIJK", "1234abcd", "1234ABCD"],
        )
        def test_when_has_no_match_regex_requirements(self, password):
            user = User()
            user.password = password

            with pytest.raises(ValueError, match="Invalid password."):
                user._User__validate_password()


class TestEmail:
    class TestSuccess:
        @pytest.mark.parametrize(
            "email", ["a@a.com", "teste,mail@teste.com", "Valid@gmail.com"]
        )
        def test_when_has_valid_email(self, email):
            user = User()
            user.email = email

            try:
                user._User__validate_email()
            except Exception as exc:
                assert False, f"'validate_email' raised an exception {exc}"

    class TestFailure:
        @pytest.mark.parametrize("email", [1, {}, [], (), 123, {"a:1"}, [1], (2, 1)])
        def test_when_is_not_string(self, email):
            user = User()
            user.email = email

            with pytest.raises(TypeError, match="Email must be a string"):
                user._User__validate_email()

        @pytest.mark.parametrize(
            "email", ["any_string", "teste@", "teste@teste", "1234"]
        )
        def test_when_not_match_regex(self, email):
            user = User()
            user.email = email

            with pytest.raises(ValueError, match="Invalid email address."):
                user._User__validate_email()
