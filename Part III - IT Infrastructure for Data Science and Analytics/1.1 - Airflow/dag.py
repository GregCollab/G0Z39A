from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime

dag = DAG(
    dag_id="modern-data-analytics",
    start_date=datetime(2024, 3, 25, 9, 0, 0),
    schedule_interval="* * * * *",
    catchup=False
)

def print_message():
    print("This is a python operator!")

python_task = PythonOperator(
    task_id="print_message",
    python_callable=print_message,
    dag=dag,
)

generate_random_number = BashOperator(
    task_id="generate_random_number",
    bash_command="echo $RANDOM",
    dag=dag,
)

notify = BashOperator(
    task_id="notify",
    bash_command='echo "Random number generated!"',
    dag=dag,
)

python_task >> generate_random_number >> notify
