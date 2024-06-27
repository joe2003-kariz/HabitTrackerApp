import sqlite3

def create_connection():
    """
    Create a connection to the SQLite database.

    :return: Connection object.
    """
    conn = sqlite3.connect('habits.db')
    return conn

def create_tables(conn):
    """
    Create tables for storing habits and completions.

    :param conn: Connection object.
    """
    with conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS habits (
                           id INTEGER PRIMARY KEY,
                           name TEXT,
                           periodicity TEXT,
                           creation_date TEXT
                        )''')
        conn.execute('''CREATE TABLE IF NOT EXISTS completions (
                           id INTEGER PRIMARY KEY,
                           habit_id INTEGER,
                           completion_date TEXT,
                           FOREIGN KEY(habit_id) REFERENCES habits(id)
                        )''')
