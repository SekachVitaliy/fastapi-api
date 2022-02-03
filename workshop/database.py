from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from workshop.settings import settings

engine = create_engine(
    settings.db_url,
    echo=True
)

Session = sessionmaker(
    engine,
)


def get_session() -> Session:
    session = Session()
    try:
        yield session
    finally:
        session.close()
