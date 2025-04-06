import sqlite3

import typer

import habitpy.backend as backend

CONNECTION = sqlite3.connect("data.db")
app = typer.Typer(no_args_is_help=True, help="CLI habit manager")


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


if __name__ == "__main__":
    backend.create_table(CONNECTION)

    app()
