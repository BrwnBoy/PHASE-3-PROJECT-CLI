# The engine & the base declarative class
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base


engine = create_engine('sqlite:///app.db')
DBSession = sessionmaker(bind=engine)
session = DBSession()


# Creating base declarative model class
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(100))
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    # Relationship Field
    subject = relationship('Subject', back_populates='users')

class Subject(Base):
    __tablename__ = 'subjects'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    users = relationship('User', back_populates='subject')

# Create the subjects
subjects = ['Mathematics', 'Languages', 'Science', 'History', 'Geography', 'Music/Arts']
for name in subjects:
    subject = Subject(name=name)
    session.add(subject)

Base.metadata.create_all(engine)
