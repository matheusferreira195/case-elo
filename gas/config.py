import os
from airflow.hooks.base import BaseHook

connection = BaseHook.get_connection("dw_elo")

class Config:
    """Basic config class. Contains data relevant to the child classes.
    """
    USER = connection.login
    PASSWORD = connection.password
    HOST = f'{connection.host}:{connection.port}'

class HomologConfig(Config):
    """Homologation environment config object.

    Args:
        Config (class): base config object
    """

    AMBIENTE = 'homolog'
    CHUNK_SIZE = 110000
    DATABASE = 'dw_elo'
class DevelopmentConfig(Config):
    """Development environment config object.

    Args:
        Config (class): base config object
    """

    AMBIENTE = 'dev'
    CHUNK_SIZE = 110000
    DATABASE = 'dw_elo'
class ProductionConfig(Config):
    """Production environment config object.

    Args:
        Config (class): base config object
    """

    AMBIENTE = 'prod'
    CHUNK_SIZE = 110000
    DATABASE = 'dw_elo'

config_by_name = dict(
    dev=DevelopmentConfig,
    homologacao=HomologConfig,
    producao=ProductionConfig
)
def get_config(ambiente_var=None):
    """Selection function that gives the corresponding environment object.

    Args:
        ambiente_var (str, optional): Environment selector. Defaults to None.

    Returns:
        Class: Object with environment variables
    """
    var = ambiente_var if ambiente_var else os.getenv('ambiente', 'dev')
    config = config_by_name[var]

    return config
 