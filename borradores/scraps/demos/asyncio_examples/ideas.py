# /// script
# requires-python = ">=3.13"
# dependencies = ["aiohttp"]
# ///

import aiohttp
import asyncio

urls = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3"
]

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()

async def main():
    async with aiohttp.ClientSession() as session:
        for result in await asyncio.gather(
            *[fetch(session, url) for url in urls]
        ):
            print(result)

asyncio.run(main())

When does gather not work? When you need conditional cancelling, depending
on where things are. Gather just cancels no matter what. Does cancelling
still do finally? Yes.

return_exceptions=True

Why use these?
Futuro/Future
Tarea/Task
Corrutina/Coroutine

ErrorGroups

TaskCancelled is a base exception

cancel related
retry some
retry others
