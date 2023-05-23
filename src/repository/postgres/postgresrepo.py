from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.repository.postgres.config import configuration
from src.repository.postgres.postgres_objects import Base


class PostgresRepo:
    def __init__(self, testing=False):
        if not testing:
            connection_string = "postgresql+psycopg2://{}:{}@{}:{}/{}".format(
                configuration["POSTGRES_USER"],
                configuration["POSTGRES_PASSWORD"],
                configuration["POSTGRES_HOSTNAME"],
                configuration["POSTGRES_PORT"],
                configuration["APPLICATION_DB"],
            )
        else:
            connection_string = "sqlite:////home/decorus/Lab/projects/python/me-corrige-ai/db1.db"
        self.engine = create_engine(connection_string)

        Base.metadata.create_all(self.engine)
        Base.metadata.bind = self.engine

    @contextmanager
    def get_session(self):
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
