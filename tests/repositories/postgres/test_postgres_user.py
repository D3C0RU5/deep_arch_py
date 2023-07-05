import pytest
from app.repositories.postgres.user import UserPostgresRepository


def test_get(pg_session, pg_test_data):
    repo = UserPostgresRepository(testing=True)

    user = repo.get(id=2)

    assert user.name == pg_test_data[1]["name"]
    assert user.email == pg_test_data[1]["email"]
    assert user.avatar == pg_test_data[1]["avatar"]
