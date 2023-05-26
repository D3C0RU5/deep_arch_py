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

    def create(self, user_to_insert: user.User):
        new_user = User(
            code=str(user_to_insert.code),
            name=user_to_insert.name,
            login=user_to_insert.login,
            password=user_to_insert.password,
            email=user_to_insert.email,
        )
        with self.get_session() as session:
            session.add(new_user)
            session.flush()
            created_user = user.User(
                code=new_user.code,
                name=new_user.name,
                login=new_user.login,
                password=new_user.password,
                email=new_user.email,
            )

        return created_user
