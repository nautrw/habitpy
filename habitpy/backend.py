def create_table(connection):
    cursor = connection.cursor()

    cursor.execute(
        """
                   CREATE TABLE IF NOT EXISTS habits
                   (name TEXT, times INTEGER, last_modified INTEGER)
                   """
    )

    connection.commit()
    cursor.close()
