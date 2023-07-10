from abc import ABC, abstractmethod

from app.core.entities.user import UserEntity
from app.core.repositories import BaseRepositoryInterface


class UserRepositoryInterface(BaseRepositoryInterface, ABC):
    @abstractmethod
    def get_by_name(self, name: str) -> UserEntity:
        ...
