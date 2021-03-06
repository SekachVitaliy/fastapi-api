import os
import sys
import pytest

# Устанавливаем `os.environ`, чтобы использовать тестовую БД
from fastapi.testclient import TestClient
from workshop.app import app
os.environ['TESTING'] = 'TRUE'
from alembic import command
from alembic.config import Config
from workshop.settings import settings
from sqlalchemy_utils import create_database, drop_database


@pytest.fixture(scope="module")
def temp_db():
    # create_database(settings.db_url)  # Создаем БД
    # base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    # alembic_cfg = Config(os.path.join(base_dir, "workshop\\alembic.ini"))  # Загружаем конфигурацию alembic
    # command.upgrade(alembic_cfg, "head")  # выполняем миграции
    pass

    try:
        yield settings.db_url
    finally:
        pass
        # drop_database(settings.db_url)  # удаляем БД


@pytest.fixture(scope="function")
def client() -> TestClient:
    return TestClient(app)
