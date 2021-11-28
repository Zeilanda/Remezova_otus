"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
from typing import List

import aiohttp
import asyncio


USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def get_users() -> List[dict]:
    async with aiohttp.ClientSession() as session:
        async with session.get(USERS_DATA_URL) as response:

            print('Status', response.status)
            print('Content-type:', response.headers['content-type'])

            html = await response.json()
            return html


async def get_posts() -> List[dict]:
    async with aiohttp.ClientSession() as session:
        async with session.get(POSTS_DATA_URL) as response:

            print('Status', response.status)
            print('Content-type:', response.headers['content-type'])

            html = await response.json()
            return html


# async def run_main():
#     await fetch_users()
#     await fetch_posts()
#
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(run_main())
