import time


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


def create_habit(connection, name):
    cursor = connection.cursor()

    time_started = int(time.time())

    cursor.execute(
        "INSERT INTO habit VALUES(?, ?, ?, ?)",
        (name, 0, time_started, time_started),
    )

    connection.commit()
    cursor.close()


def delete_habit(connection, id):
    cursor = connection.cursor()

    cursor.execute("DELETE FROM habit WHERE rowid=?", (id,))

    connection.commit()
    cursor.close()


def rename_habit(connection, id, new_name):
    cursor = connection.cursor()

    current_time = time.time()

    cursor.execute(
        "UPDATE habit SET name=?, last_modified=? WHERE rowid=?",
        (new_name, current_time, id),
    )

    connection.commit()
    cursor.close()
