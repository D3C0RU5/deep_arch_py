from abc import ABCMeta, abstractmethod


class BaseUseCase(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, *args, **kwargs):
        ...
