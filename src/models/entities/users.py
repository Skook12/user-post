# pylint:disable=R0903

from sqlalchemy import Column,String, Integer, Float
from src.models.connection.base import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    person_name = Column(String, nullable=False)
    age = Column(Integer)
    height = Column(Float)

    def __repr__(self):
        return f"Users [id={self.id}, person_name={self.person_name}]"