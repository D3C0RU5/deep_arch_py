from abc import ABC
from contextlib import contextmanager
from typing import List, Optional

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.entities import BaseEntity

from app.repositories import BaseRepository
from app.repositories.postgres.base import Base


configuration = {
    "POSTGRES_USER": "pguser",
    "POSTGRES_PASSWORD": "postgres",
    "POSTGRES_HOSTNAME": "localhost",
    "POSTGRES_PORT": "5432",
    "APPLICATION_DB": "db-postgres",
}


class PostgresRepository(BaseRepository, ABC):
    def __init__(self, testing=False) -> None:
        self.Instance: Base

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

    def list(self) -> List[BaseEntity]:
        with self.get_session() as session:
            results = [
                result.to_entity() for result in session.query(self.Instance).all()
            ]

        return results

    def add(self, other: BaseEntity) -> BaseEntity:
        new_instance: Base = self.Instance.from_dict(other.to_dict())
        with self.get_session() as session:
            session.add(new_instance)
            session.flush()
            result = new_instance.to_entity()

        return result

    def delete(self, id: str) -> bool:
        entity_exists = None

        with self.get_session() as session:
            db_register = session.get(self.Instance, id)
            if db_register:
                session.delete(db_register)
                entity_exists = True
            else:
                entity_exists = False

        return entity_exists
