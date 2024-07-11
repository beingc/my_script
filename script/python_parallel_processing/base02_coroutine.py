import asyncio
import aiohttp
import time

urls = [
    'https://jsonplaceholder.typicode.com/posts/1',
    'https://jsonplaceholder.typicode.com/posts/2',
    'https://jsonplaceholder.typicode.com/posts/3',
    'https://jsonplaceholder.typicode.com/posts/4',
    'https://jsonplaceholder.typicode.com/posts/5'
]


# 协程方式获取数据
async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def main():
    start_time = time.time()
    # Gather all coroutine tasks for fetching data
    tasks = [fetch_data(url) for url in urls]
    results = await asyncio.gather(*tasks)
    end_time = time.time()

    print("Results with coroutines:", results)
    print("Time taken with coroutines:", end_time - start_time, "seconds")


if __name__ == '__main__':
    asyncio.run(main())
