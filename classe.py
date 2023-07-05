from abc import ABC


class A:
    pass


class C:
    pass


class Pai(ABC):
    def __init__(self):
        print(self.Instance)


class Filho(Pai, ABC):
    def __init__(self):
        self.Instance = A
        super().__init__()


Filho()
