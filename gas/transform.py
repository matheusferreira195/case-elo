import pandas as pd


def transform():

    df_leitura = pd.read_parquet('/opt/airflow/tmp/raw/leitura.parquet')

    df_medidor = pd.read_parquet('/opt/airflow/tmp/raw/medidor.parquet')
    df_medidor.drop(columns=['DT_CARGA'], inplace=True)

    df_segmento_mercado = pd.read_parquet('/opt/airflow/tmp/raw/segmento_mercado.parquet')
    df_segmento_mercado.drop(columns=['DT_CARGA'], inplace=True)

    df_tabela_resumo = df_leitura.merge(df_medidor, left_on=['SK_MEDIDOR', 'CD_MEDIDOR'], right_on=['SK_MEDIDOR', 'CD_MEDIDOR'], how='outer')
    df_tabela_resumo = df_tabela_resumo.merge(df_segmento_mercado, left_on=['SK_SEGMENTO_MERCADO'],right_on=['SK_SEGMENTO_MERCADO'], how='outer')

    df_tabela_resumo.to_parquet('/opt/airflow/tmp/trs/leitura_gas.parquet')

if __name__ == "__main__":
    transform()