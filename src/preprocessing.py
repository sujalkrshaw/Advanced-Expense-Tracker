import pandas as pd
import sqlite3

def load_data():
    conn = sqlite3.connect("data/expenses.db")
    df = pd.read_sql("SELECT * FROM expenses", conn)
    conn.close()

    df['date'] = pd.to_datetime(df['date'])
    df['amount'] = pd.to_numeric(df['amount'])

    df['month'] = df['date'].dt.month
    df['weekday'] = df['date'].dt.day_name()

    return df