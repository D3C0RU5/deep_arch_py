from abc import ABC, abstractmethod
from typing import Iterable, Optional

from app.core.entities import BaseEntity


class BaseRepositoryInterface(ABC):
    @abstractmethod
    def add(self, other: BaseEntity) -> BaseEntity:
        ...

    @abstractmethod
    def delete(self, id: str) -> bool:
        ...

    @abstractmethod
    def get(self, id: str) -> Optional[BaseEntity]:
        ...

    @abstractmethod
    def list(self) -> Iterable[BaseEntity]:
        ...
