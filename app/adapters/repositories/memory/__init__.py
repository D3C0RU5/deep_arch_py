from abc import ABC
from typing import Iterable, Optional

from app.core.entities import BaseEntity
from app.core.repositories import BaseRepositoryInterface


class MemoryRepository(BaseRepositoryInterface, ABC):
    def __init__(self) -> None:
        self.data: list[BaseEntity] = []

    def get(self, id: str) -> Optional[BaseEntity]:
        return next((e for e in self.data if e.id == id), None)

    def list(self) -> Iterable[BaseEntity]:
        return self.data

    def add(self, other: BaseEntity) -> BaseEntity:
        self.data.append(other)
        other.id = str(len(self.data))
        return other

    def delete(self, id: str) -> bool:
        self.data = list(filter(lambda e: e.id != id, self.data))
        return True
