from typing import Iterable
from app.core.entities.user import UserEntity
from app.core.repositories.user_interface import UserRepositoryInterface
from app.core.use_cases import BaseUseCase


class UserListUseCase(BaseUseCase):
    repo: UserRepositoryInterface

    def __init__(self, repo: UserRepositoryInterface) -> None:
        self.repo = repo

    def execute(self) -> Iterable[UserEntity]:
        return self.repo.list()
