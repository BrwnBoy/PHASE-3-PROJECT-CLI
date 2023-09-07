# Logics
import click
from db import Base, engine, User, Subject
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

@click.command()
@click.option('--username', prompt='PLease enter your username')
def register(username):
    # Checking if the user already exists
    user = session.query(User).filter_by(username=username).first()
    if user:
        click.echo(f'Username {username} is already taken. Please choose a different username.')
    else:
        # Creating a new user and adding them to the database
        new_user = User(username=username)
        session.add(new_user)
        session.commit()
        click.echo(f'User {username} registered successfully!')

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    register()
    select_subject()