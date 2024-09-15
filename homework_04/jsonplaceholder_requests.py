"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

import aiohttp
import asyncio



USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"
FETCH_DATA_TIMEOUT = 10



async def fetch_json(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()
        

async def fetch_users() -> list[dict]:
    users = []
    try:
        users: list[dict] = await fetch_json(USERS_DATA_URL)
    except aiohttp.ClientError as ex:
        print("Failed to fetch users", ex)

    return users


async def fetch_posts() -> list[dict]:
    posts = []
    try:
        posts: list[dict] = await fetch_json(POSTS_DATA_URL)
    except aiohttp.ClientError as ex:
        print("Failed to fetch posts", ex)

    return posts


async def fetch_data() -> tuple:
    
    async with asyncio.timeout(FETCH_DATA_TIMEOUT):
        result =  await asyncio.gather(
            fetch_users(),
            fetch_posts()
        )

    return result