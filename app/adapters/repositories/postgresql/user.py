from __future__ import annotations
from abc import ABC
from typing import List, Optional
import typing
from sqlalchemy import Column, Integer, String
from app.adapters.repositories.postgresql import PostgresRepository
from app.adapters.repositories.postgresql.base import Base

from app.core.entities.user import UserEntity
from app.core.repositories.user_interface import UserRepositoryInterface


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)

    @classmethod
    def from_dict(cls, other: dict) -> User:
        return cls(
            id=other.get("id"),
            password=other["password"],
            name=other["name"],
            email=other["email"],
        )

    def to_entity(self):
        return UserEntity(
            id=self.id,
            name=self.name,
            email=self.email,
            password=self.password,
        )


class UserPostgresRepository(PostgresRepository, UserRepositoryInterface, ABC):
    def __init__(self, testing=False):
        super().__init__(testing)
        self.Instance = User
        self.Entity = UserEntity

    if typing.TYPE_CHECKING:

        def get(self, id: str) -> Optional[UserEntity]:
            ...

        def list(self) -> List[UserEntity]:
            ...

        def add(self, other: UserEntity) -> UserEntity:
            ...

        def delete(self, id: str) -> bool:
            ...

    def get_by_name(self, name: str) -> UserEntity:
        with self.get_session() as session:
            result = (
                session.query(self.Entity).filter(User.name == name).first().to_entity()
            )

        return result
