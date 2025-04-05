import sqlite3
import time

import habitpy.backend as backend

CONNECTION = sqlite3.connect("data.db")

if __name__ == "__main__":
    backend.create_table(CONNECTION)

    backend.create_habit(CONNECTION, "test")
    backend.create_habit(CONNECTION, "test2")
    backend.rename_habit(CONNECTION, 2, "test2-renamed")
