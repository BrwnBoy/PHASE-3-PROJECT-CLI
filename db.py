# The engine & the base declarative class
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///app.db')
DBSession = sessionmaker(bind=engine)
session = DBSession()


# Creating base declarative model class
Base = declarative_base()