"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""

import asyncio

from sqlalchemy.ext.asyncio import AsyncSession

from models import User, Post, create_tables, Session
from jsonplaceholder_requests import fetch_data



async def create_user(
    name: str,
    username: str,
    email: str
):
    user = User(
        name=name,
        username=username,
        email=email
    )

    return user


async def create_post(
    title: str,
    body: str,
    user_id: int
):
    post = Post(
        title=title,
        body=body,
        user_id=user_id
    )

    return post


async def fill_in_users(
    session: AsyncSession,
    users: list[dict]
):
    users_list = []
    for user in users:
        users_list.append(await create_user(
            name=user.get("name"),
            username=user.get("username"),
            email=user.get("email")
        ))

    session.add_all(users_list)

    await session.commit()


async def fill_in_posts(
    session: AsyncSession,
    posts: list[dict]
):
    posts_list = []
    for post in posts:
        posts_list.append(await create_post(
            title=post.get("title"),
            body=post.get("body"),
            user_id=post.get("userId")
        ))

    session.add_all(posts_list)

    await session.commit()


async def fill_in_data(
        session: AsyncSession,
        users_data: list[dict],
        posts_data: list[dict]
):
    await fill_in_users(
        session=session,
        users=users_data
    )
    await fill_in_posts(
        session=session,
        posts=posts_data
    )
    await session.close()


async def async_main():
    await create_tables()

    users_data: list[dict]
    posts_data: list[dict]
    users_data, posts_data = await fetch_data()

    async with Session() as session:
        await fill_in_data(
            session=session,
            users_data=users_data,
            posts_data=posts_data
        )


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()