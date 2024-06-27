import click
from habit_manager import HabitManager
from analytics import *

manager = HabitManager()

@click.group()
def cli():
    pass

@cli.command()
def create_habit():
    name = click.prompt('Enter habit name')
    periodicity = click.prompt('Enter habit periodicity (daily/weekly)')
    manager.add_habit(name, periodicity)
    click.echo(f'Habit {name} created with periodicity {periodicity}.')

@cli.command()
def delete_habit():
    name = click.prompt('Enter habit name to delete')
    manager.delete_habit(name)
    click.echo(f'Habit {name} deleted.')

@cli.command()
def list_habits():
    habits = manager.list_habits()
    for habit in habits:
        click.echo(f'Habit: {habit.name}, Periodicity: {habit.periodicity}')

@cli.command()
def analyze_habits():
    click.echo(f'Longest Streak: {longest_run_streak(manager)}')

if __name__ == '__main__':
    cli()

