from pydantic import BaseModel, PostgresDsn, Secret


class DatabaseConfig(BaseModel):
    url: Secret[PostgresDsn]
