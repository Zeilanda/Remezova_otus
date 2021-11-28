"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import aiohttp
import asyncio


USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_users():
    async with aiohttp.ClientSession() as session:
        async with session.get(USERS_DATA_URL) as response:

            print('Status', response.status)
            print('Content-type:', response.headers['content-type'])

            html = await response.json()
            print("Body:", html)


async def fetch_posts():
    async with aiohttp.ClientSession() as session:
        async with session.get(USERS_DATA_URL) as response:

            print('Status', response.status)
            print('Content-type:', response.headers['content-type'])

            html = await response.json()
            print("Body:", html)


async def run_main():
    await fetch_users()
    await fetch_posts()


loop = asyncio.get_event_loop()
loop.run_until_complete(run_main())
