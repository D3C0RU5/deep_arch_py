import pytest
import sqlalchemy

from src.repository.postgres.postgres_objects import Base, User
from tests.repository.seed import users


@pytest.fixture(scope="session")
def pg_session_empty():
    conn_str = "sqlite:////home/decorus/Lab/projects/python/me-corrige-ai/db1.db"
    engine = sqlalchemy.create_engine(conn_str)
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
        new_user = User(
            code=r["code"],
            name=r["name"],
            login=r["login"],
            password=r["password"],
            email=r["email"],
        )
        pg_session_empty.add(new_user)
        pg_session_empty.commit()

    yield pg_session_empty

    pg_session_empty.query(User).delete()
    pg_session_empty.commit()
