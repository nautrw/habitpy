import sqlite3
from datetime import datetime
from typing import List

import typer
from rich import box
from rich.console import Console
from rich.table import Table

import habitpy.backend as backend

CONNECTION = sqlite3.connect("data.db")
app = typer.Typer(no_args_is_help=True, help="CLI habit manager")


def habits_table(all_habits: List, title: str):
    table = Table(
        "ID",
        "Name",
        "Times",
        "Date Started",
        "Last Modified",
        title=title,
        box=box.ROUNDED,
        row_styles=["", "dim"],
    )

    for habit in all_habits:
        date_started = datetime.fromtimestamp(habit[3]).strftime("%b %d, %Y")
        last_modified = datetime.fromtimestamp(habit[4]).strftime("%b %d, %Y")

        table.add_row(
            str(habit[0]),
            habit[1],
            str(habit[2]),
            date_started,
            last_modified,
        )

    return table


@app.command()
def create(name: str):
    """
    Create a habit
    """
    id = backend.create_habit(CONNECTION, name)
    fg = typer.colors.GREEN
    typer.secho(
        f"Successfully created habit '{name}' with ID {id}", fg=fg
    )  # read next comment


@app.command()
def delete(id: int):
    """
    Delete a habit
    """
    if not backend.check_exists(CONNECTION, id):
        typer.secho(f"Habit with ID {id} does not exist", fg=typer.colors.RED)
        exit()

    backend.delete_habit(CONNECTION, id)
    fg = typer.colors.GREEN
    typer.secho(
        f"Successfully deleted habit with ID {id}", fg=fg
    )  # stupid flake8 keeps bothering me


@app.command()
def get(id: int):
    """
    Get a specific habit
    """
    console = Console()
    if not backend.check_exists(CONNECTION, id):
        typer.secho(f"Habit with ID {id} does not exist", fg=typer.colors.RED)
        exit()

    habit = backend.get_habit(CONNECTION, id)
    table = habits_table([habit], title="Habit")

    console.print(table)


@app.command()
def list():
    """
    List all habits
    """
    console = Console()
    all_habits = backend.get_all_habits(CONNECTION)

    if len(all_habits) <= 0:
        typer.secho("No habits found", fg=typer.colors.RED)
        exit()

    table = habits_table(all_habits, title="All Habits")

    console.print(table)


@app.command()
def increase(id: int):
    """
    Increase the times on a habit
    """
    if not backend.check_exists(CONNECTION, id):
        typer.secho(f"Habit with ID {id} does not exist", fg=typer.colors.RED)
        exit()

    backend.change_habit_times(CONNECTION, id, 1)
    fg = typer.colors.GREEN
    typer.secho(
        f"Successfully increased times on habit with ID {id}", fg=fg
    )  # see comment above this one


@app.command()
def decrease(id: int):
    """
    Decrease the times on a habit
    """
    if not backend.check_exists(CONNECTION, id):
        typer.secho(f"Habit with ID {id} does not exist", fg=typer.colors.RED)
        exit()

    backend.change_habit_times(CONNECTION, id, -1)
    fg = typer.colors.GREEN
    typer.secho(
        f"Successfully decreased times on habit with ID {id}", fg=fg
    )  # read comment above this one


if __name__ == "__main__":
    backend.create_table(CONNECTION)

    app()
