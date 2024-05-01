import pydantic
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    DB_USER: str = pydantic.Field(alias="POSTGRES_USER")
    DB_PASSWORD: str = pydantic.Field(alias="POSTGRES_PASSWORD")
    DB_SERVER: str = pydantic.Field(alias="POSTGRES_HOST")
    DB_PORT: int = pydantic.Field(alias="POSTGRES_PORT")
    DB_NAME: str = pydantic.Field(alias="POSTGRES_DB_NAME")
