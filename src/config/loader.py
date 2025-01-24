from pydantic_settings import BaseSettings, SettingsConfigDict

from .construct_models import *


class Settings(BaseSettings):
    bot: BotConfig
    database: DatabaseConfig

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        case_sensitive=False,
        env_nested_delimiter='__',
    )


settings = Settings.model_validate({})
