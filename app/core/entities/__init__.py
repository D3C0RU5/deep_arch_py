from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from typing import Optional


@dataclass
class BaseEntity(metaclass=ABCMeta):
    id: Optional[str]

    def __post_init__(self):
        # Validate id
        if not isinstance(self.id, int) and self.id != None:
            raise TypeError("Id should be a int")

    @classmethod
    @abstractmethod
    def from_dict(cls, other: dict):
        ...

    @abstractmethod
    def to_dict(self):
        ...
