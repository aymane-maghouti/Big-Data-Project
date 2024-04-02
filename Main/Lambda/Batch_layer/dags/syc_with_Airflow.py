import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from Batch_layer.batch_layer import  batch_layer


with DAG(
    dag_id="daily_data_sync",
    start_date=datetime.datetime(2024, 3, 29),
    schedule_interval="*/1 * * * *",  # Run every 1 minutes
) as dag:
    batch_layer = PythonOperator(
        task_id="batch layer",
        python_callable=batch_layer()
    )

batch_layer