from typing import Literal

from pydantic import BaseModel, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class DBSettings(BaseModel):
    host: str = 'localhost'
    port: int = 5432
    username: str = "user"
    password: SecretStr = "secret_password"
    database_name: str = "test"
    pool_min_size: int = 5
    pool_max_size: int = 10
    pool_max_inactive_lifetime: int = 300


    @property
    def dsn(self) -> str:
        return f"{self.provider}://{self.user}:{self.password}@{self.host}:{self.port}/{self.database_name}?async_fallback=True"


class JWTSettings(BaseModel):
    secret_key: str = "your_jwt_secret_key"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 15
    refresh_token_expire_minutes: int = 120


class RedisSettings(BaseSettings):
    host: str = "localhost"
    port: int = 6379
    db: int = 3


class Settings(BaseSettings):
    db: DBSettings
    jwt: JWTSettings

    env: Literal["dev", "prod"] = "dev"

    model_config = SettingsConfigDict(
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        case_sensitive=False,
        extra="ignore",
    )


async def get_settings() -> Settings:
    return Settings()

