from abc import ABC

from app.adapters.repositories.memory import MemoryRepository
from app.core.entities.user import UserEntity
from app.core.repositories.user_interface import UserRepositoryInterface


class UserMemoryRepository(MemoryRepository, UserRepositoryInterface, ABC):
    def get_by_name(self, name: str) -> UserEntity:
        return next((e for e in self.data if e.name == name), None)
