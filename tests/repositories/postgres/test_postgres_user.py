from faker import Faker
from app.entities.user import UserEntity
from app.repositories.postgres.user import UserPostgresRepository

faker = Faker()


def test_get(pg_session, pg_test_data):
    repo = UserPostgresRepository(testing=True)

    user = repo.get(id=2)

    assert user.name == pg_test_data[1]["name"]
    assert user.email == pg_test_data[1]["email"]
    assert user.avatar == pg_test_data[1]["avatar"]


def test_list(pg_session, pg_test_data):
    repo = UserPostgresRepository(testing=True)

    users = repo.list()

    assert len(users) == len(pg_test_data)


def test_add(pg_session, pg_test_data):
    repo = UserPostgresRepository(testing=True)
    user = UserEntity.from_dict(
        {
            "name": faker.name(),
            "email": faker.email(),
            "avatar": faker.file_path(category="image"),
        }
    )

    new_user = repo.add(user)

    assert new_user.id == 4
    assert new_user.name == user.name
    assert new_user.email == user.email
    assert new_user.avatar == user.avatar


class TestDelete:
    def test_success_when_id_exists(self, pg_session, pg_test_data):
        repo = UserPostgresRepository(testing=True)
        deleted = repo.delete(2)

        assert deleted is True

    def test_success_when_not_exists(self, pg_session, pg_test_data):
        repo = UserPostgresRepository(testing=True)
        deleted = repo.delete(99)

        assert deleted is False
