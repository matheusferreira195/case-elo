import os

class Config:
    USER = 'postgres'
    PASSWORD = 'processo-elo'
    HOST = 'elodb:5432'

class HomologConfig(Config):
    AMBIENTE = 'homolog'
    CHUNK_SIZE = 110000
    DATABASE = 'dw_elo'
    TABLENAME = 'CONSUMO_VAREJO_EUROMONITOR'
    STORAGE_PATH = '/storage'
class DevelopmentConfig(Config):
    AMBIENTE = 'dev'
    CHUNK_SIZE = 110000
    DATABASE = 'dw_elo'
    TABLENAME = 'CONSUMO_VAREJO_EUROMONITOR'

class ProductionConfig(Config):
    AMBIENTE = 'prod'
    CHUNK_SIZE = 110000
    DATABASE = 'dw_elo'
    TABLENAME = 'CONSUMO_VAREJO_EUROMONITOR'

config_by_name = dict(
    dev=DevelopmentConfig,
    homologacao=HomologConfig,
    producao=ProductionConfig
)
def get_config(ambiente_var=None):
    var = ambiente_var if ambiente_var else os.getenv('ambiente', 'dev')
    config = config_by_name[var]

    return config
 