from random import randrange
import pytest
from app.adapters.repositories.memory.user import UserMemoryRepository

from app.core.entities.user import UserEntity


@pytest.fixture
def data(user_factory) -> list[UserEntity]:
    data: list[UserEntity] = []
    for i in range(1, 10):
        entity = user_factory()
        data.append(entity)

    return data


class TestMemoryRepository:
    class TestGetByName:
        def test_return_first_item(self, data: list[UserEntity]):
            repository = UserMemoryRepository()
            repository.data = data

            result = repository.get_by_name(repository.data[0].name)

            assert isinstance(result, UserEntity)
            assert data is not None
            assert result.to_dict() == repository.data[0].to_dict()
