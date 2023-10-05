import re
from typing import Optional, TypedDict

from pydantic import validator, EmailStr

from app.core.entities import BaseEntity


class UserEntity(BaseEntity):
    name: str
    email: EmailStr
    password: str

    @validator("name")
    def name_validation(cls, name):
        if not isinstance(name, str):
            raise TypeError("Name should be a string")

        return name

    @validator("password")
    def password_validation(cls, password):
        if not 8 <= len(password) <= 12:
            raise ValueError("Password length should be between 8 and 12 characters.")

        return password
