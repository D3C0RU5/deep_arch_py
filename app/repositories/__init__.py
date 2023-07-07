from abc import ABC, abstractmethod
from typing import Iterable, Optional

from app.entities import BaseEntity


class BaseReadOnlyRepository(ABC):
    @abstractmethod
    def get(self, id: str) -> Optional[BaseEntity]:
        ...

    @abstractmethod
    def list(self) -> Iterable[BaseEntity]:
        ...


class BaseWriteOnlyRepository(ABC):
    @abstractmethod
    def add(self, other: BaseEntity) -> BaseEntity:
        ...

    @abstractmethod
    def delete(self, id: str) -> bool:
        ...


class BaseRepository(BaseReadOnlyRepository, BaseWriteOnlyRepository, ABC):
    ...
