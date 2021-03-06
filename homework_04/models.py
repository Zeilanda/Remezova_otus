"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os
from sqlalchemy import (Column, String, Integer, ForeignKey, Text)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, relationship

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://user:password@localhost/postgres"

engine = create_async_engine(PG_CONN_URI, echo=True)

Base = declarative_base()

Session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


class User(Base):

    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), default='')
    username = Column(String(32), unique=True)
    email = Column(String(32), unique=True)

    posts = relationship("Post", back_populates='user')

    # def __str__(self):
    #     return f"{self.__class__.__name__}(id={self.id}, " \
    #            f"username={self.username!r}, is_staff={self.is_staff})"


class Post(Base):

    __tablename__ = 'Post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("User.id"), nullable=False)
    title = Column(String(256), nullable=False, default='', server_default='')
    body = Column(Text, nullable=False, default="", server_default="")

    user = relationship("User", back_populates='posts')
