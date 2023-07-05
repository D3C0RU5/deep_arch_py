from app.repositories.postgres.user import UserPostgresRepository


def test_get(pg_session, pg_test_data):
    repo = UserPostgresRepository(testing=True)

    user = repo.get(id=1)

    assert user.to_dict()["name"] == pg_test_data[0]["name"]
    assert user.to_dict()["email"] == pg_test_data[0]["email"]
    assert user.to_dict()["avatar"] == pg_test_data[0]["avatar"]
