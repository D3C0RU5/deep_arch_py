from abc import ABC
from typing import Iterable, Optional

from sqlalchemy import Column, Integer, String
from app.entities.user import UserEntity
from app.repositories.postgres import Base, PostgresRepository
from app.repositories.user_interface import UserRepository


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    avatar = Column(String, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    @classmethod
    def from_dict(cls, other: dict):
        return cls(
            id=other.get("id"),
            avatar=other["avatar"],
            name=other["name"],
            email=other["email"],
        )

    def to_dict(self):
        dict_to_return = {}
        for k, v in self.__dict__.items():
            if k != "_sa_instance_state" and k != "id":
                dict_to_return[k] = v

        return dict_to_return

    def to_entity(self):
        return UserEntity(
            id=self.id,
            name=self.name,
            email=self.email,
            avatar=self.avatar,
        )


class UserPostgresRepository(PostgresRepository, UserRepository, ABC):
    def __init__(self, testing=False):
        self.Instance = User
        self.Entity = UserEntity
        super().__init__(testing)

    # def get(self, id: str) -> Optional[UserEntity]:
    #     pass
    #     # with self.get_session() as session:
    #     #     result = session.query(User).filter(User.id == id).first()

    #     # return UserEntity.from_dict(result.to_dict())

    def list(self) -> Iterable[UserEntity]:
        pass
        # with self.get_session() as session:
        #     results = session.query(User).all()

        # return [UserEntity.from_dict(item.to_dict()) for item in results]

    def add(self, other: UserEntity):
        pass
        # new_register = User()
        # with self.get_session() as session:
        #     results = session.query(User).all()

    def remove(self, id: str) -> bool:
        pass

    def get_by_name(self, name: str) -> UserEntity:
        pass
