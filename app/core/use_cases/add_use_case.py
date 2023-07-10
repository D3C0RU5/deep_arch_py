from app.core.entities.user import UserEntity
from app.core.repositories.user_interface import UserRepositoryInterface
from app.core.use_cases import BaseUseCase


class UserAddUseCase(BaseUseCase):
    repo: UserRepositoryInterface

    def __init__(self, repo: UserRepositoryInterface) -> None:
        self.repo = repo

    def execute(self, user: UserEntity) -> UserEntity:
        return self.repo.add(user)
