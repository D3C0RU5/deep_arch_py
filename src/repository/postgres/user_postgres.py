from repository.postgres.postgres_objects import User
from repository.postgres.postgresrepo import PostgresRepo
from domain.user import User as UserDomain


class UserPostgresRepo(PostgresRepo):
    def _create_objects(self, results):
        return [UserDomain(**q.to_dict()) for q in results]

    def list_users(self):
        with self.get_session() as session:
            results = self._create_objects(session.query(User).all())

        return results

    def create(self, user_to_insert: UserDomain):
        new_user = User(**user_to_insert.to_dict())
        with self.get_session() as session:
            session.add(new_user)

        return True
