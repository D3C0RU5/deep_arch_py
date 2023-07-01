import uuid

from faker import Faker
from domain import user
from src.repository.postgres.user_postgres import UserPostgresRepo

faker = Faker()


class TestList:
    def test_list_users(self, pg_session, pg_test_data):
        repo_users = UserPostgresRepo(testing=True)

        users = repo_users.list_users()

        assert set([str(r.code) for r in users]) == set(
            [r["code"] for r in pg_test_data]
        )


class TestCreate:
    def test_create_user(self, pg_session_empty):
        repo_users = UserPostgresRepo(testing=True)

        user_to_be_created = user.User(
            code=uuid.uuid4(),
            name=faker.name(),
            login=faker.word(),
            password=faker.password(),
            email=faker.email(),
        )

        is_user_created = repo_users.create(user_to_be_created)

        assert is_user_created
