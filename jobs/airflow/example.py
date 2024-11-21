from airflow.decorators import dag, task
from datetime import datetime

@task
def first_task():
    print(1)


@dag(schedule_interval='@daily', start_date=datetime(2024, 1, 1), catchup=False)
def first_job():

    first_task()

first_job()
