from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor

default_args = {
    "owner": "Dan", 
    "retries": 5, 
    "retry_delay": timedelta(minutes=5)}

with DAG(
    default_args = default_args,
    dag_id = "dag_with_MinIO_S3",
    start_date = datetime(2023, 2, 18, 4),
    schedule_interval= "@daily"
    ) as dag:
    task1 = S3KeySensor(
        task_id = "MinIO_S3_Sensor", 
        bucket_name = "airflow-bucket", 
        bucket_key = "data.csv", 
        aws_conn_id = "minio_conn",
        mode = "poke",
        poke_interval = 5,
        timeout = 30)