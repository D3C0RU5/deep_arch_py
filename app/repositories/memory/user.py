from app.entities.user import UserEntity
from app.repositories.memory import MemoryRepository


class UserMemoryRepository(MemoryRepository):
    def get_by_name(self, name: str) -> UserEntity:
        return next((e for e in self.data if e.name == name), None)
