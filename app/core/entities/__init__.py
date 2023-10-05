from abc import ABCMeta, abstractmethod
from typing import Optional

from pydantic import BaseModel, validator


class BaseEntity(BaseModel, metaclass=ABCMeta):
    id: Optional[int]

    @validator("id")
    def id_validation(cls, v):
        if not isinstance(v, int) and v != None:
            raise TypeError("Id should not be a int")
