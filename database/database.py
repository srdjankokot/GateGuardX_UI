import sqlite3


class Database:
    def __init__(self, db_path="gateguardx.db"):
        self.db_path = db_path
        self.init_db()

    def init_db(self):
        """
        Initialize the database and create the table if it doesn't exist.
        """
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS controllers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                role TEXT NOT NULL,
                api_url TEXT NOT NULL,
                linked_cameras TEXT
            )
            """
        )
        connection.commit()
        connection.close()

    def fetch_all(self):
        """
        Fetch all rows from the database.
        """
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute("SELECT id, name, role, api_url, linked_cameras FROM controllers")
        rows = cursor.fetchall()
        connection.close()
        return rows

    def fetch_one(self, row_id):
        """
        Fetch a single row by ID.
        """
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute("SELECT name, role, api_url, linked_cameras FROM controllers WHERE id = ?", (row_id,))
        row = cursor.fetchone()
        connection.close()
        return row

    def insert(self, name, role, api_url, linked_cameras):
        """
        Insert a new row into the database.
        """
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO controllers (name, role, api_url, linked_cameras)
            VALUES (?, ?, ?, ?)
            """,
            (name, role, api_url, linked_cameras),
        )
        connection.commit()
        connection.close()

    def update(self, row_id, name, role, api_url, linked_cameras):
        """
        Update an existing row in the database.
        """
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute(
            """
            UPDATE controllers
            SET name = ?, role = ?, api_url = ?, linked_cameras = ?
            WHERE id = ?
            """,
            (name, role, api_url, linked_cameras, row_id),
        )
        connection.commit()
        connection.close()

    def delete(self, row_id):
        """
        Delete a row from the database by ID.
        """
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute("DELETE FROM controllers WHERE id = ?", (row_id,))
        connection.commit()
        connection.close()
