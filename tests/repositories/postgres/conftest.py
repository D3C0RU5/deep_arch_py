import pytest
import sqlalchemy

from app.repositories.postgres import Base
from app.repositories.postgres.user import User
from tests.repositories.seed import users


@pytest.fixture(scope="session")
def pg_session_empty():
    connection_string = (
        "sqlite:////home/decorus/Lab/projects/python/deep-arch/sqlite.db"
    )
    engine = sqlalchemy.create_engine(connection_string)
    connection = engine.connect()

    Base.metadata.create_all(engine)
    Base.metadata.bind = engine

    DBSession = sqlalchemy.orm.sessionmaker(bind=engine)
    session = DBSession()

    yield session

    session.close()
    connection.close()


@pytest.fixture(scope="session")
def pg_test_data():
    return users


@pytest.fixture(scope="function")
def pg_session(pg_session_empty, pg_test_data):
    for r in pg_test_data:
        pg_session_empty.add(
            User(
                name=r["name"],
                avatar=r["avatar"],
                email=r["email"],
            )
        )
        pg_session_empty.commit()

    yield pg_session_empty

    pg_session_empty.query(User).delete()
    pg_session_empty.commit()
