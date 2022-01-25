from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from gas.extract import get_dados_leitura, get_dados_medidor, get_dados_segmento_mercado
from gas.transform import transform
from gas.load import load_tabela_segmento_d, load_tabela_leitura_f, load_tabela_geral_f, load_tabela_medidor_d

with DAG(
    dag_id='gas_cabecoes_sa',
    schedule_interval='0 0 * * *',
    start_date=datetime(2021, 1, 1),
    catchup=False,
    dagrun_timeout=timedelta(minutes=60),
    tags=['cabecoes_sa', 'gas'],
) as dag:

    task_get_dados_leitura = PythonOperator(
        task_id='get_dados_leitura',
        python_callable=get_dados_leitura
    )

    task_get_dados_medidor = PythonOperator(
        task_id='get_dados_medidor',
        python_callable=get_dados_medidor
    )

    task_get_dados_segmento_mercado = PythonOperator(
        task_id='get_dados_segmento_mercado',
        python_callable=get_dados_segmento_mercado
    )

    task_transform = PythonOperator(
        task_id='transform_dados',
        python_callable=transform
    )

    [task_get_dados_leitura, task_get_dados_medidor, task_get_dados_segmento_mercado] >> task_transform

    task_load_tabela_segmento_d = PythonOperator(
        task_id='load_tabela_segmento_d',
        python_callable=load_tabela_segmento_d
    )

    task_load_tabela_leitura_f = PythonOperator(
        task_id='load_tabela_leitura_f',
        python_callable=load_tabela_leitura_f
    )

    task_load_tabela_geral_f = PythonOperator(
        task_id='load_tabela_geral_f',
        python_callable=load_tabela_geral_f
    )

    task_load_tabela_medidor_d = PythonOperator(
        task_id='load_tabela_medidor_d',
        python_callable=load_tabela_medidor_d
    )

    task_transform >> [task_load_tabela_segmento_d, task_load_tabela_leitura_f, task_load_tabela_medidor_d, task_load_tabela_geral_f]

if __name__ == "__main__":
    dag.cli()