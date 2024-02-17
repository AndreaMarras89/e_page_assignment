"""Application settings"""

from pydantic_settings import BaseSettings


class Configuration(BaseSettings):
    database_url: str = "postgresql+asyncpg://user:pass123@localhost:5432/postgres"
    server_port: int = 8088
    default_timeout: int = 30
    default_workers: int = 1
    log_level: str = "info"


config = Configuration()
