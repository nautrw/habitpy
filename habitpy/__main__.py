import sqlite3
import time

import habitpy.backend as backend

CONNECTION = sqlite3.connect("data.db")

if __name__ == "__main__":
    backend.create_table(CONNECTION)

    backend.create_habit(CONNECTION, "test", 0, time.time(), time.time())
    backend.create_habit(CONNECTION, "test2", 0, time.time(), time.time())
    backend.delete_habit(CONNECTION, 1)
