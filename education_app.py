# Logics
import click
from db import User, Subject, session

@click.command()
def register_user():
    username = input("Enter your name: ")
    user = User(username=username)
    session.add(user)
    session.commit()
    print("You've registered successfuly!")

@click.command()
def list_subjects():
    subjects = session.query(Subject).all()
    if subjects:
        for subject in subjects:
            print(subject.name)
    else:
        print("No subjects found in the database.")

@click.group()
def cli():
    pass

cli.add_command(register_user)
cli.add_command(list_subjects)

if __name__ == '__main__':
    cli()