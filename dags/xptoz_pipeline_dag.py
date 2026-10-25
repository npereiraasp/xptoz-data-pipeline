# Databricks notebook source
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'xptoz_daily_pipeline',
    default_args=default_args,
    description='Pipeline for XPTOZ data engineering challenge',
    schedule='@daily',
    catchup=False,
) as dag:

    # Tarefa 1: Executa o script Python para ingestão e atualização dos dados na camada Raw
    run_ingestion = BashOperator(
        task_id='generate_and_load_raw_data',
        bash_command='pip install faker psycopg2-binary pandas sqlalchemy && python /opt/airflow/dags/scripts/generate_data.py'
    )

    # Tarefa 2: Executa os modelos do DBT respeitando as dependências das camadas
    run_dbt = BashOperator(
        task_id='run_dbt_models',
        bash_command='pip install dbt-postgres && cd /opt/airflow/dags/dbt_xptoz && dbt run --profiles-dir .'
    )

    # Definindo a ordem de execução (Dependência estrita)
    run_ingestion >> run_dbt