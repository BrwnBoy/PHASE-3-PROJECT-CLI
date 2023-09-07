from sqlalchemy import Column, Integer, String, ForeignKey
from db import Base, engine

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(100), null=False)
