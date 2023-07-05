from random import randrange
from faker import Faker
import pytest
from app.entities.user import UserEntity
from app.repositories.memory.user import UserMemoryRepository

faker = Faker()


def create_entity(id: int):
    return UserEntity.from_dict(
        {
            "id": id,
            "name": faker.name(),
            "email": faker.email(),
            "avatar": faker.file_path(category="image"),
        }
    )


@pytest.fixture
def data() -> list[UserEntity]:
    data: list[UserEntity] = []
    for i in range(randrange(1, 10)):
        entity = create_entity(i + 1)
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
