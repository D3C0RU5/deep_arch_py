import pytest
from app.repositories.postgres.user import UserPostgresRepository


@pytest.mark.parametrize("id, index", [(1, 0), (2, 1)])
def test_get(pg_session, pg_test_data, id, index):
    repo = UserPostgresRepository(testing=True)

    user = repo.get(id=id)

    assert user.name == pg_test_data[index]["name"]
    assert user.email == pg_test_data[index]["email"]
    assert user.avatar == pg_test_data[index]["avatar"]
