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

from jsonplaceholder_requests import fetch_users_data, fetch_posts_data
from models import engine, Base, User, Post


async def create_tables():
    """"
    If we aren't using alembic
    :return:
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


# async def create_some_users():
#     user_sam = User(name='Sam', username='sam', email='sam11@example.com')
#     user_ann = User(name='Ann', username='annie', email='annie56@example.com')
#     async with async_session() as session:  # type: AsyncSession
#         async with session.begin():
#             session.add_all([
#                 user_sam,
#                 user_ann,
#                 User(name='John', username='john', email='john2@example.com')
#             ])
#     print('user sam', user_sam)
#
#
# async def create_post_for_users():
#     # stmt_q_users = select(User)
#     stmt_user_sam = select(User).where(User.username == 'sam')
#     stmt_user_ann = select(User).where(User.username == 'john')
#     stmt_user_john = select(User).where(User.username == 'annie')
#
#     async with async_session() as session:  # type: AsyncSession
#         async with session.begin():
#             user_sam = (await session.execute(stmt_user_sam)).scalar_one_or_none()
#             user_ann = (await session.execute(stmt_user_ann)).scalar_one_or_none()
#             user_john = (await session.execute(stmt_user_john)).scalar_one_or_none()
#             print(user_sam)
#             print(user_john)
#             post_dodge_and_burn = Post(title='Dodge&Burn',
#                                        body='Dodging and burning are terms used in photography...',
#                                        user_id=user_sam
#                                        )
#
#             post_image_editing = Post(title='Image editing',
#                                       body='Image editing encompasses the processes of altering images...',
#                                       author=user_john
#                                       )
#
#             session.add_all([
#                 Post(
#                     title='Color adjustments',
#                     body='The color of images can be altered in a variety of ways.',
#                     author=user_ann),
#                 post_dodge_and_burn,
#                 post_image_editing
#             ])


async def async_main():
    await create_tables()
    await asyncio.gather(fetch_users_data(), fetch_posts_data())


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
