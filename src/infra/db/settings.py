from functools import cache

from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL


@cache
class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8'
    )

    database_hostname: str = 'localhost'
    database_port: int = 5432
    database_password: str = 'admin'
    database_username: str = 'postgres'
    database_name: str = 'postgres'

    @computed_field
    @property
    def url(self) -> URL:
        return URL.create(
            'postgresql+psycopg',
            username=self.database_username,
            password=self.database_password,
            host=self.database_hostname,
            port=self.database_port,
            database=self.database_name,
        )
