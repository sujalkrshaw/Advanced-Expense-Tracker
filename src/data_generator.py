import pandas as pd
import numpy as np
import sqlite3

def generate_data():
    np.random.seed(42)

    dates = pd.date_range(start="2024-01-01", periods=200)
    categories = ["Food", "Travel", "Rent", "Shopping", "Bills"]
    types = ["Expense", "Income"]

    data = pd.DataFrame({
        "date": np.random.choice(dates, 300),
        "category": np.random.choice(categories, 300),
        "amount": np.random.randint(100, 5000, 300),
        "type": np.random.choice(types, 300)
    })

    conn = sqlite3.connect("data/expenses.db")
    data.to_sql("expenses", conn, if_exists="replace", index=False)
    conn.close()

    print("Data inserted into database")