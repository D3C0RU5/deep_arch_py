class InvalidResquest:
    def __init__(self) -> None:
        self.errors = []

    def add_error(self,parameter,message) -> None:
        self.errors.append({"parameter":parameter, "message":message})

    def has_errors(self) -> bool:
        return len(self.errors) > 0

    def __bool__(self) -> bool:
        return False
