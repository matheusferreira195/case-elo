from sqlalchemy import create_engine

def get_connection_postgres(config):
    engine = create_engine(f'postgresql://{config.USER}:{config.PASSWORD}@{config.HOST}/{config.DATABASE}')

    return engine
