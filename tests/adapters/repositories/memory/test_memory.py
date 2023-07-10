from dataclasses import dataclass
from random import randrange
from typing import Optional, TypedDict
from faker import Faker
import pytest
from app.adapters.repositories.memory import MemoryRepository

from app.core.entities import BaseEntity

faker = Faker()


class Dummy(TypedDict):
    id: Optional[int]


@dataclass
class DummyEntity(BaseEntity):
    @classmethod
    def from_dict(cls, other: dict):
        return cls(id=other["id"])

    def to_dict(self) -> Dummy:
        return {"id": self.id}


def create_entity(id: int):
    return DummyEntity.from_dict({"id": id})


@pytest.fixture
def data() -> list[BaseEntity]:
    data: list[BaseEntity] = []
    for i in range(randrange(1, 10)):
        entity = create_entity(i + 1)
        data.append(entity)

    return data


class TestMemoryRepository:
    class TestGet:
        def test_return_first_item(self, data: list[BaseEntity]):
            repository = MemoryRepository()
            repository.data = data

            result = repository.get(repository.data[0].id)

            assert isinstance(result, DummyEntity)
            assert data is not None
            assert result.to_dict() == repository.data[0].to_dict()

    class TestList:
        def test_return_filled_list(self, data: list[BaseEntity]):
            repository = MemoryRepository()
            repository.data = data

            result = repository.list()

            isinstance(result, list)
            assert len(result) == len(data)

        def test_return_empty_list(self):
            repository = MemoryRepository()

            result = repository.list()

            assert isinstance(result, list)
            assert len(result) == 0

    class TestAdd:
        def test_add_on_empty_list(self):
            repository = MemoryRepository()
            dummy_entity = create_entity(1)

            result = repository.add(dummy_entity)

            assert result == dummy_entity
            assert repository.data[0] == dummy_entity
            assert len(repository.data) == 1

        def test_add_on_filled_list(self, data: list[BaseEntity]):
            repository = MemoryRepository()
            repository.data = data
            initial_data_len = len(data)

            dummy_entity = create_entity(1)

            result = repository.add(dummy_entity)

            assert result == dummy_entity
            assert repository.data[-1] == dummy_entity
            assert len(repository.data) == initial_data_len + 1

    class TestDelete:
        def test_delete_item(self, data: list[BaseEntity]):
            repository = MemoryRepository()
            repository.data = data
            initial_data_len = len(data)
            last_item = data[-1]

            result = repository.delete(last_item.id)

            assert result is True
            assert len(repository.data) is initial_data_len - 1
