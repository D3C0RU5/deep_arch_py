import dataclasses
import re
from typing import Optional
import uuid

from domain.base_domain import BaseDomain


@dataclasses.dataclass
class User(BaseDomain):
    code: Optional[str] = None
    name: Optional[str] = None
    login: Optional[str] = None
    password: Optional[str] = None
    email: Optional[str] = None

    def __validate_code(self):
        try:
            if self.code is None:
                self.code = uuid.uuid4()
                return
            if isinstance(self.code, str):
                try:
                    self.code = uuid.UUID(self.code)
                except:
                    raise ValueError("Badly formed hexadecimal UUID string")
            elif not isinstance(self.code, uuid.UUID):
                raise TypeError("Code must be an UUID")
        except Exception as exc:
            self.add_error(exc)

    def __validate_name(self):
        try:
            if self.name is None:
                return
            if not isinstance(self.name, str):
                raise TypeError("Name must be a string")
        except Exception as exc:
            self.add_error(exc)

    def __validate_login(self):
        try:
            if self.login is None:
                return
            if not isinstance(self.login, str):
                raise TypeError("Login must be a string")
            if not len(self.login) > 5 and not len(self.login) < 15:
                raise TypeError("The size of login must be lower than 15")
        except Exception as exc:
            self.add_error(exc)

    def __validate_password(self):
        try:
            if self.password is None:
                return
            if not isinstance(self.password, str):
                raise TypeError("Password must be a string")
            if not re.match(
                r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$", self.password
            ):
                raise ValueError("Invalid password.")
        except Exception as exc:
            self.add_error(exc)

    def __validate_email(self):
        try:
            if self.email is None:
                return
            if not isinstance(self.email, str):
                raise TypeError("Email must be a string")
            if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
                raise ValueError("Invalid email address.")
        except Exception as exc:
            self.add_error(exc)

    def __post_init__(self):
        self.__validate_code()
        self.__validate_name()
        self.__validate_login()
        self.__validate_password()
        self.__validate_email()

    def to_dict(self):
        dict_to_return = self.__dict__.copy()
        dict_to_return["code"] = str(self.code)
        return dict_to_return
