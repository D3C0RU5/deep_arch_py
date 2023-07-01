import dataclasses

from src.utils.requests import InvalidResquest, ValidRequest


@dataclasses.dataclass(init=False)
class BaseDomain:
    def __init__(self) -> None:
        self._errors = []

    @classmethod
    def from_dict(cls, dict):
        return cls(**dict)

    def to_dict(self):
        return dataclasses.asdict(self)

    def add_error(self, exception: Exception):
        return self._errors.append(exception)

    def get_error_as_dict(self, index):
        error = self._errors[index]
        return {
            "parameter": type(error).__name__,
            "message": str(error),
        }

    def has_errors(self):
        return len(self._errors) > 0

    def get_request(self):
        if self.has_errors():
            request = InvalidResquest()
            request.add_errors(self._errors)

            return request

        return ValidRequest(body=self)
