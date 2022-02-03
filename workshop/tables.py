import sqlalchemy as sa
from sqlalchemy import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user_db'
    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.String)
    email = sa.Column(sa.String)
    password = sa.Column(sa.String)
    register_data = sa.Column(sa.DateTime, server_default=func.now())
