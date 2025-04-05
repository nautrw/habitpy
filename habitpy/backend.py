def create_table(connection):
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS habit
            (name TEXT,
             times INTEGER,
             started INTEGER,
             last_modified INTEGER)
        """
    )

    connection.commit()
    cursor.close()


def create_habit(connection, name, times, started, last_modified):
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO habit VALUES(?, ?, ?, ?)",
        (name, times, last_modified, started),
    )

    connection.commit()
    cursor.close()


def delete_habit(connection, id):
    cursor = connection.cursor()

    cursor.execute("DELETE FROM habit WHERE rowid=?", (id,))

    connection.commit()
    cursor.close()
