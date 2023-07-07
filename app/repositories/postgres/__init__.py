import abc
from contextlib import contextmanager
from typing import Optional

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, DeclarativeMeta
from app.entities import BaseEntity

from app.repositories import BaseRepository


configuration = {
    "POSTGRES_USER": "pguser",
    "POSTGRES_PASSWORD": "postgres",
    "POSTGRES_HOSTNAME": "localhost",
    "POSTGRES_PORT": "5432",
    "APPLICATION_DB": "db-postgres",
}


class PostgresRepository(BaseRepository, abc.ABC):
    def __init__(self, testing=False) -> None:
        if not testing:
            connection_string = "postgresql+psycopg2://{}:{}@{}:{}/{}".format(
                configuration["POSTGRES_USER"],
                configuration["POSTGRES_PASSWORD"],
                configuration["POSTGRES_HOSTNAME"],
                configuration["POSTGRES_PORT"],
                configuration["APPLICATION_DB"],
            )
        else:
            connection_string = (
                "sqlite:////home/decorus/Lab/projects/python/deep-arch/sqlite.db"
            )
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

    def get(self, id: str) -> Optional[BaseEntity]:
        with self.get_session() as session:
            result = session.get(self.Instance, id).to_entity()

        return result

    def list(self) -> Optional[BaseEntity]:
        with self.get_session() as session:
            results = [
                result.to_entity() for result in session.query(self.Instance).all()
            ]

        return results


class DeclarativeABCMeta(DeclarativeMeta, abc.ABCMeta):
    pass


class Base(declarative_base(metaclass=DeclarativeABCMeta)):
    __abstract__ = True

    @classmethod
    @abc.abstractmethod
    def from_dict(cls, other: dict):
        ...

    @abc.abstractmethod
    def to_entity(self):
        ...

    def to_dict(self):
        dict_to_return = {}
        for k, v in self.__dict__.items():
            if k != "_sa_instance_state":
                dict_to_return[k] = v

        return dict_to_return
