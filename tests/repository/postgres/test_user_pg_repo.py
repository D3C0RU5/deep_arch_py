from src.repository.postgres.user_postgres import UserPostgresRepo


def test_repository_list_users(pg_session, pg_test_data,):
    repo_users = UserPostgresRepo(testing=True)

    users = repo_users.list()

    assert set([r.code for r in users]) == set(
        [r["code"] for r in pg_test_data])
