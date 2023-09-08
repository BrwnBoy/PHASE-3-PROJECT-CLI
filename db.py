# The engine & the base declarative class
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Creating the engine
engine = create_engine('sqlite:///app.db')

# Creating a session factory
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Creating the base declarative model class
Base = declarative_base()

# Defining the Subject model
class Subject(Base):
    __tablename__ = 'subjects'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    # Relationship Field
    users = relationship('User', back_populates='subjects')

# Defining the User model
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(100))
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    
    # Relationship Field
    subjects = relationship('Subject', back_populates='users')

# Creating the tables
Base.metadata.create_all(engine)

# Inserting subjects into the 'subjects' table
subjects = ['Mathematics', 'Languages', 'Science', 'History', 'Geography', 'Music/Arts']
for name in subjects:
# Checking if subject already exists
    subject = session.query(Subject).filter_by(name=name).first()
    
    if subject:
        pass
    else:
        subject = Subject(name=name)
        session.add(subject)

session.commit()

# Closing the session
session.close()
