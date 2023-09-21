import os
from logging import config as logging_config
from typing import Optional

from pydantic import BaseSettings, Field

from core.logger import LOGGING

logging_config.dictConfig(LOGGING)


class Settings(BaseSettings):
    POSTGRES_DB: str = Field('postgres', env='POSTGRES_DB')
    POSTGRES_USER: str = Field('postgres', env='POSTGRES_USER')
    POSTGRES_PASSWORD: str = Field('postgres', env='POSTGRES_PASSWORD')
    POSTGRES_HOST: str = Field('localhost', env='POSTGRES_HOST')
    POSTGRES_PORT: int = Field('5432', env='POSTGRES_PORT')

    PROJECT_NAME: str = Field(..., env='PROJECT_NAME')
    PROJECT_DESCRIPTION: str = Field(..., env='PROJECT_DESCRIPTION')
    PROJECT_VERSION: str = Field(..., env='PROJECT_VERSION')

    BASE_DIR: Optional[str] = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    class Config:
        env_file = '.env'


settings = Settings()
