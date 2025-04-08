import sqlite3
from datetime import datetime

import typer
from rich import box
from rich.console import Console
from rich.table import Table

import habitpy.backend as backend

CONNECTION = sqlite3.connect("data.db")
app = typer.Typer(no_args_is_help=True, help="CLI habit manager")
console = Console()


@app.command()
def create(name: str):
    """
    Create a habit
    """
    id = backend.create_habit(CONNECTION, name)
    print(f"Successfuly created habit '{name}' with ID {id}")


@app.command()
def delete(id: int):
    """
    Delete a habit
    """
    backend.delete_habit(CONNECTION, id)
    print(f"Successfuly deleted habit with ID {id}")


@app.command()
def list():
    """
    List all habits
    """
    all_habits = backend.get_all_habits(CONNECTION)

    if len(all_habits) <= 0:
        print("No habits found")
        exit()

    table = Table(title="All habits", box=box.ROUNDED)
    table.add_column("ID")
    table.add_column("Name")
    table.add_column("Times")
    table.add_column("Date Started")
    table.add_column("Last Modified")

    for habit in all_habits:
        date_started = datetime.fromtimestamp(habit[3]).strftime("%b %d, %Y")
        last_modified = datetime.fromtimestamp(habit[4]).strftime("%b %d, %Y")

        table.add_row(
            str(habit[0]),
            str(habit[1]),
            str(habit[2]),
            str(date_started),
            str(last_modified),
        )

    console.print(table)


if __name__ == "__main__":
    backend.create_table(CONNECTION)

    app()
