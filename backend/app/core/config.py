from typing import Optional

from pydantic import BaseSettings, PostgresDsn, validator


class Config(BaseSettings):
    BASE_CLIENT_URL: str
    API_V1: str = "/api/v1"

    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_DSN: Optional[PostgresDsn] = None

    @validator("POSTGRES_DSN", pre=True)
    def build_db_connection_str(
        cls, v: Optional[str], values: dict[str, Optional[str]]
    ) -> Optional[str]:
        if isinstance(v, str):
            return v
        else:
            return PostgresDsn.build(
                scheme="postgresql",
                user=values.get("POSTGRES_USER"),
                password=values.get("POSTGRES_PASSWORD"),
                host=values.get("POSTGRES_HOST"),
                port=values.get("POSTGRES_PORT"),
                path=f'/{values.get("POSTGRES_DB", "")}',
            )


config = Config()
