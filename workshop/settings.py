from pydantic import BaseSettings
from environs import Env

env = Env()
env.read_env()

DB_USER = env.str("DB_USER")
DB_PASS = env.str("DB_PASS")
DB_NAME = env.str("DB_NAME")
DB_HOST = env.str("DB_HOST")
TESTING = env.bool("TESTING")
if TESTING:
    DB_NAME = "db-for-test"


class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = '8000'
    db_url: str = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8',
)
