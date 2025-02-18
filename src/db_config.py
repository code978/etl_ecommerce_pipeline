import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()
database_url = os.getenv("connection_string")


db_path = "./data/ecommerce_sales.db"

# Ensure the 'data' directory exists
os.makedirs(os.path.dirname(db_path), exist_ok=True)

def get_db_engine(db_type="sqlite"):
    if db_type == "sqlite":
        return create_engine(f"sqlite:///{db_path}")
    elif db_type == "postgres":
        return create_engine(database_url)    
    else:
        raise ValueError("Invalid database type. Use 'sqlite' or 'postgres'.")

# Example usage
engine = get_db_engine("sqlite")
