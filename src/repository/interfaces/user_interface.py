from abc import ABC, abstractmethod

from src.repository.postgres.postgres_objects import User


class UserInterface(ABC):
    @abstractmethod
    def list_users(self) -> list[User]:
        raise Exception("Should implement method: list_users")

    @abstractmethod
    def create(self) -> bool:
        raise Exception("Should implement method: create")
