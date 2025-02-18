import pandas as pd
from sqlalchemy import create_engine
from db_config import get_db_engine
import os

db_path = "./data/ecommerce_sales.db"

# Ensure the 'data' directory exists
os.makedirs(os.path.dirname(db_path), exist_ok=True)


df = pd.read_csv("./data/ecommerce_sales_data.csv")

# Standardize column names
df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]

# Convert 'order_date' column to YYYY-MM-DD format
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce').dt.strftime('%Y-%m-%d')

# Remove duplicates
df.drop_duplicates(inplace=True)

# Handle missing values
df.fillna({'quantity': 0, 'price': 0}, inplace=True)

# Calculate total revenue if not present
if 'total_revenue' not in df.columns:
    df['total_revenue'] = df['quantity'] * df['price_per_unit']

# Create revenue per product table
revenue_per_product = df.groupby('product_id')['total_revenue'].sum().reset_index()

# Create orders per customer table
orders_per_customer = df.groupby('customer_id')['order_id'].nunique().reset_index()

# Connect to database (SQLite for local testing, PostgreSQL for production)
engine = get_db_engine("postgres")
# Load data into database


df.to_sql('sales', engine, if_exists='replace', index=False)
revenue_per_product.to_sql('revenue_per_product', engine, if_exists='replace', index=False)
orders_per_customer.to_sql('orders_per_customer', engine, if_exists='replace', index=False)

print("ETL process completed successfully!")
