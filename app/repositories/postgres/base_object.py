from abc import ABC, abstractmethod


class BaseObject(ABC):
    @classmethod
    @abstractmethod
    def from_dict(cls, other: dict):
        ...

    @abstractmethod
    def to_entity(self):
        ...

    def to_dict(self):
        dict_to_return = {}
        for k, v in self.__dict__.items():
            if k != "_sa_instance_state":
                dict_to_return[k] = v

        return dict_to_return
