from functools import cache

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

    url: URL = URL.create(
        'postgresql+psycopg',
        username=database_username,
        password=database_password,
        host=database_hostname,
        port=database_port,
        database=database_name,
    )
