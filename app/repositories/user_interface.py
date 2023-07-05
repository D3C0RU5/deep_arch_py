from abc import ABC, abstractmethod

from app.entities.user import UserEntity


class UserRepository(ABC):
    @abstractmethod
    def get_by_name(self, name: str) -> UserEntity:
        ...
