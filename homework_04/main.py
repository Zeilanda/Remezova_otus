"""
Домашнее задание №3
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

from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_session, AsyncSession

from jsonplaceholder_requests import users_data, posts_data
from models import engine, Base, User, Post, Session


async def create_tables():
    """"
    If we aren't using alembic
    :return:
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def add_users():
    users_list = []
    for user in await users_data():
        user_bd = User(id=user['id'], name=user['name'], username=user['username'], email=user['email'])
        users_list.append(user_bd)
    async with Session() as session:  # type: AsyncSession
        async with session.begin():
            session.add_all(users_list)


async def add_post():
    posts_list = []
    for post in await posts_data():
        post_bd = Post(id=post['id'], user_id=post['userId'], title=post['title'], body=post['body'])
        posts_list.append(post_bd)
    async with Session() as session:  # type: AsyncSession
        async with session.begin():
            session.add_all(posts_list)


async def async_main():
    await create_tables()
    await asyncio.gather(
        add_users(),
        add_post(),
    )


def main():
    asyncio.get_event_loop().run_until_complete(async_main())


if __name__ == "__main__":
    main()
