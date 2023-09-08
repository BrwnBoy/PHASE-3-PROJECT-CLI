# Logics
import click
import random
from db import User, Subject, session, Base, engine

command_history = []

@click.command()
def register_user():
    username = click.prompt("Enter your name")
    user = User(username=username)
    session.add(user)
    session.commit()
    command_history.append("register_user")
    print("You've registered successfuly!")

@click.command()
def list_subjects():
    subjects = session.query(Subject).all()
    if subjects:
        for subject in subjects:
            click.echo(subject.name)
    else:
        click.echo("No subjects found in the database.")
    command_history.append("list_subjects")

questions = [
       {"question": "What is the capital of France?", "answer": "Paris"},
       {"question": "Who painted the Mona Lisa?", "answer": "Leonardo Da Vinci"},
       {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"}
]

@click.command()
def quiz():
    question = random.choice(questions)
    user_answer = click.prompt(question["question"])

    if user_answer.lower() == question["answer"].lower():
        click.echo("You are correct!")
    else:
        click.echo("You are wrong!")

@click.command()
def show_history():
    unique_commands = list(set(command_history))
    if unique_commands:
        click.echo("Command History:")
        for command in unique_commands:
            click.echo(command)
    else:
        click.echo("No command history found.")

@click.group()
def cli():
    pass

cli.add_command(register_user)
cli.add_command(list_subjects)
cli.add_command(quiz)
cli.add_command(show_history)

if __name__ == '__main__':
    cli()