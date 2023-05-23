import dataclasses


@dataclasses.dataclass
class BaseDomain:
    @classmethod
    def from_dict(cls, dict):
        return cls(**dict)

    def to_dict(self):
        return dataclasses.asdict(self)
