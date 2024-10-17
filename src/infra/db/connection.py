from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.infra.db.settings import Settings


class DBConnectionHandler:
    def __init__(self):
        self.__connection_url = Settings().url
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        return create_engine(self.__connection_url)

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        Session = sessionmaker(bind=self.get_engine(), autocommit=False)
        self.session = Session()
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
