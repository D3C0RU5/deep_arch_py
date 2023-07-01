from typing import Type
from src.domain.user import User as UserDomain
from src.repository.interfaces.user_interface import UserInterface
from src.utils.requests import InvalidResquest, ValidRequest
from src.utils.responses import (
    ResponseFailure,
    ResponseSuccess,
    ResponseType,
    build_invalid_response,
)


class SignUpUseCase:
    def __init__(self, user_repository: Type[UserInterface]):
        self.user_repository = user_repository

    def handle(self, name: str, login: str, password: str, email: str):
        request = UserDomain(
            name=name,
            login=login,
            password=password,
            email=email,
        ).get_request()

        if request.has_errors():
            return build_invalid_response(request)

        try:
            user = self.user_repository.create(request.body)
        except Exception as exc:
            return ResponseFailure(ResponseType.SYSTEM_ERROR, exc)

        return ResponseSuccess(user)
