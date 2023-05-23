from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    code = Column(String(36), nullable=False)
    name = Column(String, nullable=False)
    login = Column(String(15), nullable=False)
    password = Column(String(36), nullable=False)
    email = Column(String, nullable=False)
