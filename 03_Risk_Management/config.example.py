from typing import Any

from pydantic_settings import BaseSettings, SettingsConfigDict


class DBSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="QFIN_DB_",
        extra="ignore",
    )

    host: str = "localhost"
    port: int = 3306
    database: str = "market_data"
    user: str = "root"
    password: str = ""

    def as_mapping(self) -> dict[str, Any]:
        return {
            "host": self.host,
            "port": self.port,
            "database": self.database,
            "user": self.user,
            "password": self.password,
        }


DB_CONFIG = DBSettings().as_mapping()
