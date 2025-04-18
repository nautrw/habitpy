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

    lastrowid = cursor.lastrowid
    return lastrowid


def delete_habit(connection, id):
    cursor = connection.cursor()

    cursor.execute("DELETE FROM habit WHERE rowid=?", (id,))

    connection.commit()
    cursor.close()


def rename_habit(connection, id, new_name):
    cursor = connection.cursor()

    current_time = int(time.time())

    cursor.execute(
        "UPDATE habit SET name=?, last_modified=? WHERE rowid=?",
        (new_name, current_time, id),
    )

    connection.commit()
    cursor.close()


def change_habit_times(connection, id, change):
    cursor = connection.cursor()

    current_time = int(time.time())

    cursor.execute(
        "UPDATE habit SET times=times+?, last_modified=? WHERE rowid=?",
        (change, current_time, id),
    )

    connection.commit()
    cursor.close()


def get_all_habits(connection):
    cursor = connection.cursor()

    response = cursor.execute(
        "SELECT rowid, * FROM habit ORDER BY rowid ASC"
    ).fetchall()

    cursor.close()
    return response


def check_exists(connection, id):
    cursor = connection.cursor()

    results = cursor.execute(
        "SELECT * FROM habit WHERE rowid=?", (id,)).fetchall()

    cursor.close()
    return len(results) >= 1


def get_habit(connection, id):
    cursor = connection.cursor()

    response = cursor.execute(
        "SELECT rowid, * FROM habit WHERE rowid=?", (id,)
    ).fetchone()

    cursor.close()
    return response
