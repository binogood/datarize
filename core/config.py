import os

from pydantic import BaseSettings


class Config(BaseSettings):
    ENV: str = "development"
    DEBUG: bool = True
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    DB_URL: str = f"mysql+pymysql://root:poiu1234@localhost:3306/datarize"
    JWT_SECRET_KEY: str = "fastapi"
    JWT_ALGORITHM: str = "HS256"


class DevelopmentConfig(Config):
    DB_URL: str = f"mysql+pymysql://root:poiu1234@localhost:3306/datarize"

class LocalConfig(Config):
    DB_URL: str = f"mysql+pymysql://root:poiu1234@localhost:3306/datarize"

def get_config():
    env = os.getenv("EVN", "development")
    config_type = {
        "development": DevelopmentConfig(),
        "local": LocalConfig(),
    }
    return config_type[env]


config = get_config()

