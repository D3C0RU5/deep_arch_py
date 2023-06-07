from src.repository.postgres.postgres_objects import User
from src.repository.postgres.postgresrepo import PostgresRepo
from src.domain import user


class UserPostgresRepo(PostgresRepo):
    def _create_objects(self, results):
        return [
            user.User(**q.to_dict())
            for q in results
        ]

    def list(self):
        with self.get_session() as session:
            results = self._create_objects(session.query(User).all())

        return results

    def create(self, user_to_insert: user.User):
        new_user = User(**user_to_insert.to_dict())
        with self.get_session() as session:
            session.add(new_user)
            created_user = user.User(**new_user.to_dict())

        return created_user
