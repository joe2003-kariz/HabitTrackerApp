import sqlite3

def create_connection():
    conn = sqlite3.connect('habits.db')
    return conn

def create_tables(conn):
    with conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS habits (
                           id INTEGER PRIMARY KEY,
                           name TEXT,
                           periodicity TEXT,pipi
                           creation_date TEXT
                        )''')
        conn.execute('''CREATE TABLE IF NOT EXISTS completions (
                           id INTEGER PRIMARY KEY,
                           habit_id INTEGER,
                           completion_date TEXT,
                           FOREIGN KEY(habit_id) REFERENCES habits(id)
                        )''')
