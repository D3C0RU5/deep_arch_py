import re
from dataclasses import dataclass
from typing import Optional, TypedDict

from app.core.entities import BaseEntity


class UserType(TypedDict):
    id: Optional[int]
    name: str
    email: str
    password: str


@dataclass
class UserEntity(BaseEntity):
    name: str
    email: str
    password: str

    def __post_init__(self):
        # Validate name
        if not isinstance(self.name, str):
            raise TypeError("Name should be a string")

        # Validate email
        if not isinstance(self.email, str):
            raise TypeError("Age should be an string")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
            raise ValueError("Invalid email address.")

        # Validate password
        if not 8 <= len(self.password) <= 12:
            raise ValueError("Password length should be between 8 and 12 characters.")

    @classmethod
    def from_dict(cls, other: dict):
        return cls(
            id=other.get("id"),
            password=other["password"],
            name=other["name"],
            email=other["email"],
        )

    def to_dict(self) -> UserType:
        return {
            "id": self.id,
            "name": self.name,
            "password": self.password,
            "email": self.email,
        }
