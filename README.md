# ETL Pipeline for E-Commerce Sales Data

## Overview
This project extracts, transforms, and loads e-commerce sales data into a database for analysis.

## Installation

### 1. Clone the Repository

git clone https://github.com/yourusername/etl_ecommerce_pipeline.git cd etl_ecommerce_pipeline


### 2. Install Dependencies

pip install -r requirements.txt

Need to create .env file and pass connection_string

### 3. Run the ETL Pipeline
python src/etl_pipeline.py


## SQL Queries
You can execute the queries in `sql_queries/insights.sql` to analyze the data.

## Future Improvements
- Implement Apache Airflow for scheduling.
- Deploy the pipeline on AWS.
- Use Docker for containerization.


docker-compose.yml (Optional - If Using Docker)
