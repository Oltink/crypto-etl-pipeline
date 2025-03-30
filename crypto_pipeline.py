from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import requests
import psycopg2

DB_CONFIG = {
    "dbname": "crypto_db",
    "user": "postgres",
    "password": "password",
    "host": "postgres_db",
    "port": 5432
}

def fetch_crypto_prices():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    response = requests.get(url)
    print("API Response:", response.text) 
    return response.json()

def save_to_postgres(**kwargs):
    data = kwargs["ti"].xcom_pull(task_ids="fetch_prices")
    if not data:
        raise ValueError("XCom data is missing")

    print("Data received from XCom:", data) 

    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS crypto_prices (
            id SERIAL PRIMARY KEY,
            name TEXT,
            price_usd FLOAT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    for coin, values in data.items():
        cursor.execute(
            "INSERT INTO crypto_prices (name, price_usd) VALUES (%s, %s)",
            (coin, values["usd"])
        )

    conn.commit()
    cursor.close()
    conn.close()
    print("Data successfully saved to PostgreSQL") 

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 2, 1),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG(
    "crypto_price_pipeline",
    default_args=default_args,
    schedule_interval=timedelta(hours=1),
    catchup=False
)

fetch_task = PythonOperator(
    task_id="fetch_prices",
    python_callable=fetch_crypto_prices,
    dag=dag
)

save_task = PythonOperator(
    task_id="save_prices",
    python_callable=save_to_postgres,
    provide_context=True,
    dag=dag
)

fetch_task >> save_task

