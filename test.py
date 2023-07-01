import dataclasses
from typing import List


@dataclasses.dataclass()
class BaseDomain:
    errors = None


a = BaseDomain()
a.errors = 1

print(BaseDomain.errors)
