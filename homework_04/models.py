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

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker
)
from sqlalchemy.orm import (
    declarative_base,
    Mapped,
    relationship
)
from sqlalchemy import (
    Integer,
    String,
    ForeignKey,
    Column
)



PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"



async_engine = create_async_engine(PG_CONN_URI, echo=True)
Session = async_sessionmaker(bind=async_engine, expire_on_commit=False)


Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = Column(Integer, primary_key=True)
    name: Mapped[str] = Column(String)
    username: Mapped[str] = Column(String, unique=True)
    email: Mapped[str] = Column(String, unique=True)
    posts: Mapped[list["Post"]] = relationship("Post", back_populates="user")


class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = Column(Integer, primary_key=True)
    title: Mapped[str] = Column(String, unique=True)
    body: Mapped[str] = Column(String)
    user_id: Mapped[int] = Column(Integer, ForeignKey("users.id"))
    user: Mapped[User] = relationship("User", back_populates="posts")


async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)