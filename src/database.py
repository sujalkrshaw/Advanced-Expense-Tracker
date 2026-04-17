import sqlite3

def create_connection():
    conn = sqlite3.connect("data/expenses.db")
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        category TEXT,
        amount REAL,
        type TEXT
    )
    """)

    conn.commit()
    conn.close()
    