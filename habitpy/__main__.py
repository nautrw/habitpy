import sqlite3

import habitpy.backend as backend

CONNECTION = sqlite3.connect("data.db")

if __name__ == "__main__":
    backend.create_table(CONNECTION)
