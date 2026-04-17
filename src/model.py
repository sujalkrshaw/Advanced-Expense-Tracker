import os
from sklearn.linear_model import LinearRegression
import numpy as np
import joblib

def train_model(df):
    df = df[df['type'] == 'Expense']

    X = df[['month']]
    y = df['amount']

    model = LinearRegression()
    model.fit(X, y)


    model_dir = os.path.join(os.getcwd(), "models")
    os.makedirs(model_dir, exist_ok=True)

    model_path = os.path.join(model_dir, "model.pkl")

    joblib.dump(model, model_path)

def predict(month):
    model_path = os.path.join(os.getcwd(), "models", "model.pkl")
    model = joblib.load(model_path)
    return model.predict([[month]])[0]