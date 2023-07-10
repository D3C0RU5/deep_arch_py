import pytest
import sqlalchemy
from app.adapters.repositories.postgresql.base import Base
from app.adapters.repositories.postgresql.user import User

from tests.adapters.repositories.seed import users


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


def cleaning_db(session):
    session.query(User).delete()
    session.commit()


@pytest.fixture(scope="function")
def pg_session(pg_session_empty, pg_test_data):
    # Cleaning database has garbage
    cleaning_db(pg_session_empty)

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

    cleaning_db(pg_session_empty)
