
import dataclasses
import re
from typing import Optional
import uuid

from src.domain.base_domain import BaseDomain


@dataclasses.dataclass
class User(BaseDomain):
    code: Optional[str] = None
    name: Optional[str] = None
    login: Optional[str] = None
    password: Optional[str] = None
    email: Optional[str] = None

    def __validate_code(self):
        if self.code is None:
            self.code = uuid.uuid4()
            return

        if isinstance(self.code, str):
            try:
                self.code = uuid.UUID(self.code)
            except:
                raise ValueError('Badly formed hexadecimal UUID string')
        elif not isinstance(self.code, uuid.UUID):
            raise TypeError('Code must be an UUID')

    def __validate_name(self):
        if self.name is None:
            return
        if not isinstance(self.name, str):
            raise TypeError('Name must be a string')

    def __validate_login(self):
        if self.login is None:
            return
        if not isinstance(self.login, str):
            raise TypeError('Login must be a string')
        if not len(self.login) > 5 and not len(self.login) < 15:
            raise TypeError('The size of login must be lower than 15')

    def __validate_password(self):
        if self.password is None:
            return
        if not isinstance(self.password, str):
            raise TypeError('Password must be a string')
        if not re.match(r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$", self.password):
            raise ValueError("Invalid password.")

    def __validate_email(self):
        if self.email is None:
            return
        if not isinstance(self.email, str):
            raise TypeError('Email must be a string')
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
            raise ValueError("Invalid email address.")

    def __post_init__(self):
        self.__validate_code()
        self.__validate_name()
        self.__validate_login()
        self.__validate_password()
        self.__validate_email()
