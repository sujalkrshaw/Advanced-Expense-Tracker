from src.database import create_table
from src.data_generator import generate_data
from src.preprocessing import load_data
from src.model import train_model

create_table()
generate_data()

df = load_data()

train_model(df)

print("Setup complete!")