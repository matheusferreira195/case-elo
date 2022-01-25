import pandas as pd
from gas.helpers.connection import get_connection_postgres
from gas.config import get_config

config = get_config('dev')

def load_tabela_geral_f():
    """Loads the data into the target database. 
    """

    con = get_connection_postgres(config)    
    df_leitura_gas = pd.read_parquet('/opt/airflow/tmp/trs/leitura_gas.parquet')
    df_leitura_gas.to_sql('GAS_TABELA_GERAL_F', con, schema='trs', if_exists='replace')

def load_tabela_leitura_f():
    """Loads the data into the target database. 
    """

    con = get_connection_postgres(config)
    df_leitura_gas = pd.read_parquet('/opt/airflow/tmp/raw/leitura.parquet')
    df_leitura_gas.to_sql('GAS_LEITURA_F', con, schema='trs', if_exists='replace')

def load_tabela_medidor_d():
    """Loads the data into the target database. 
    """

    con = get_connection_postgres(config)
    df_leitura_gas = pd.read_parquet('/opt/airflow/tmp/raw/medidor.parquet')
    df_leitura_gas.to_sql('GAS_MEDIDOR_D', con, schema='trs', if_exists='replace')

def load_tabela_segmento_d():
    """Loads the data into the target database. 
    """
    
    con = get_connection_postgres(config)
    df_leitura_gas = pd.read_parquet('/opt/airflow/tmp/raw/segmento_mercado.parquet')
    df_leitura_gas.to_sql('GAS_SEGMENTO_D', con, schema='trs', if_exists='replace')

if __name__ == "__main__":
    """Debug purposes.
    """
    
    load_tabela_geral_f()
    load_tabela_leitura_f()
    load_tabela_medidor_d()
    load_tabela_segmento_d()