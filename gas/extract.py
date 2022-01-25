import pandas as pd

def get_dados(path_in, path_out, dict_dtype):

    df = pd.read_excel(path_in, dtype=dict_dtype)
    df.to_parquet(path_out)

def get_dados_medidor():

    dict_dtype = {
        'SK_MEDIDOR':str,
        'CD_MEDIDOR':str,
        'NR_SERIE_MEDIDOR':str,
        'CD_LOCAL_INSTALACAO':str,
        'DS_FABRICANTE':str,
        'DS_MEDIDOR':str,
        'DT_CARGA':str
    }
    
    path_in = '/opt/airflow/tmp/landing/Medidor.xlsx'
    path_out = '/opt/airflow/tmp/raw/medidor.parquet'
    
    get_dados(path_in, path_out, dict_dtype)

def get_dados_leitura():

    dict_dtype = {
        'CD_DOCUMENTO_LEITURA':str,
        'SK_SEGMENTO_MERCADO':str,
        'SK_INSTALACAO':str,
        'SK_MEDIDOR':str,
        'SK_MOTIVO_LEITURA':str,
        'SK_NOTA_LEITURISTA':str,
        'SK_STATUS_LEITURA':str,
        'CD_MEDIDOR':str,
        'CD_MOTIVO_LEITURA':str,
        'CD_MODIFICADO_POR':str,
        'CD_STATUS_LEITURA':str,
        'CD_REGISTRADOR':str,
        'QT_CONTADOR':str, 
        'DT_CARGA':str
    }
    
    path_in = '/opt/airflow/tmp/landing/Leitura.xlsx'
    path_out = '/opt/airflow/tmp/raw/leitura.parquet'
    
    get_dados(path_in, path_out, dict_dtype)

def get_dados_segmento_mercado():
    
    dict_dtype = {
        'SK_SEGMENTO_MERCADO':str,
        'CD_SEGMENTO_MERCADO':str,
        'DT_CARGA':str
    }   

    path_in = '/opt/airflow/tmp/landing/Segmento Mercado.xlsx'
    path_out = '/opt/airflow/tmp/raw/segmento_mercado.parquet'

    get_dados(path_in, path_out, dict_dtype)

if __name__ == "__main__":
    get_dados_segmento_mercado()
    get_dados_leitura()
    get_dados_medidor()
