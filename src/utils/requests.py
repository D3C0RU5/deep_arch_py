from abc import ABC


class RequestInterface(ABC):
    def __bool__(self) -> bool:
        raise Exception("Should implement method: __bool__")


class InvalidResquest(RequestInterface):
    def __init__(self) -> None:
        self.errors = []

    def add_error(self, parameter, message) -> None:
        self.errors.append({"parameter": parameter, "message": message})

    def add_errors(self, errors: list[Exception]) -> None:
        self.errors += [
            {
                "parameter": type(error).__name__,
                "message": str(error),
            }
            for error in errors
        ]

    def has_errors(self) -> bool:
        return len(self.errors) > 0

    def __bool__(self) -> bool:
        return False


class ValidRequest(RequestInterface):
    def __init__(self, body: dict) -> None:
        self.body = body

    def __bool__(self) -> bool:
        return True
