from abc import ABC
from app.entities.user import UserEntity
from app.repositories.memory import MemoryRepository
from app.repositories.user_interface import UserRepository


class UserMemoryRepository(MemoryRepository, UserRepository, ABC):
    def get_by_name(self, name: str) -> UserEntity:
        return next((e for e in self.data if e.name == name), None)
