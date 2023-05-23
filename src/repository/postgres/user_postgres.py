from src.repository.postgres.postgres_objects import User
from src.repository.postgres.postgresrepo import PostgresRepo
from src.domain import user


class UserPostgresRepo(PostgresRepo):
    def _create_objects(self, results):
        return [
            user.User(
                code=q.code,
                name=q.name,
                login=q.login,
                password=q.password,
                email=q.email,
            )
            for q in results
        ]

    def list(self):
        with self.get_session() as session:
            results = self._create_objects(session.query(User).all())

        return results
