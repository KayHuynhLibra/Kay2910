"""
Bài tập 17: Async

Mục tiêu:
- Hiểu cách làm việc với async/await
- Thực hành với asyncio
- Sử dụng async libraries
"""

import asyncio
import aiohttp
import aiofiles
import aioredis
from datetime import datetime
import json
import logging
from typing import List, Dict, Any

# TODO: Async function
async def async_function():
    """
    Basic async function
    """
    print("Starting async function")
    await asyncio.sleep(1)
    print("Async function completed")

# TODO: Async with context manager
class AsyncContextManager:
    """
    Async context manager
    """
    async def __aenter__(self):
        print("Entering async context")
        await asyncio.sleep(1)
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Exiting async context")
        await asyncio.sleep(1)

# TODO: Async HTTP client
async def fetch_url(session: aiohttp.ClientSession, url: str) -> str:
    """
    Fetch URL asynchronously
    """
    async with session.get(url) as response:
        return await response.text()

async def fetch_multiple_urls(urls: List[str]) -> List[str]:
    """
    Fetch multiple URLs concurrently
    """
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        return await asyncio.gather(*tasks)

# TODO: Async file operations
async def read_file(filename: str) -> str:
    """
    Read file asynchronously
    """
    async with aiofiles.open(filename, mode='r') as f:
        return await f.read()

async def write_file(filename: str, content: str):
    """
    Write file asynchronously
    """
    async with aiofiles.open(filename, mode='w') as f:
        await f.write(content)

# TODO: Async Redis operations
async def redis_operations():
    """
    Redis operations asynchronously
    """
    redis = await aioredis.create_redis_pool('redis://localhost')
    
    # Set value
    await redis.set('key', 'value')
    
    # Get value
    value = await redis.get('key')
    
    # Delete value
    await redis.delete('key')
    
    redis.close()
    await redis.wait_closed()

# TODO: Async database operations
class AsyncDatabase:
    """
    Async database operations
    """
    def __init__(self):
        self.data = {}
    
    async def create(self, key: str, value: Any):
        """
        Create record
        """
        await asyncio.sleep(0.1)
        self.data[key] = value
    
    async def read(self, key: str) -> Any:
        """
        Read record
        """
        await asyncio.sleep(0.1)
        return self.data.get(key)
    
    async def update(self, key: str, value: Any):
        """
        Update record
        """
        await asyncio.sleep(0.1)
        if key in self.data:
            self.data[key] = value
    
    async def delete(self, key: str):
        """
        Delete record
        """
        await asyncio.sleep(0.1)
        if key in self.data:
            del self.data[key]

# TODO: Async queue
class AsyncQueue:
    """
    Async queue implementation
    """
    def __init__(self):
        self.queue = asyncio.Queue()
    
    async def put(self, item: Any):
        """
        Put item in queue
        """
        await self.queue.put(item)
    
    async def get(self) -> Any:
        """
        Get item from queue
        """
        return await self.queue.get()
    
    async def task_done(self):
        """
        Mark task as done
        """
        self.queue.task_done()
    
    async def join(self):
        """
        Wait until queue is empty
        """
        await self.queue.join()

# TODO: Async producer-consumer
async def producer(queue: AsyncQueue, items: List[Any]):
    """
    Producer coroutine
    """
    for item in items:
        await queue.put(item)
        await asyncio.sleep(0.1)

async def consumer(queue: AsyncQueue):
    """
    Consumer coroutine
    """
    while True:
        item = await queue.get()
        print(f"Processing item: {item}")
        await asyncio.sleep(0.1)
        await queue.task_done()

# TODO: Async logging
class AsyncLogger:
    """
    Async logging implementation
    """
    def __init__(self, filename: str):
        self.filename = filename
        self.queue = asyncio.Queue()
        self.running = True
    
    async def start(self):
        """
        Start logging
        """
        while self.running:
            message = await self.queue.get()
            async with aiofiles.open(self.filename, mode='a') as f:
                await f.write(f"{datetime.utcnow()}: {message}\n")
            await self.queue.task_done()
    
    async def log(self, message: str):
        """
        Log message
        """
        await self.queue.put(message)
    
    async def stop(self):
        """
        Stop logging
        """
        self.running = False
        await self.queue.join()

# TODO: Async error handling
async def error_handling():
    """
    Async error handling
    """
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get('http://invalid-url') as response:
                return await response.text()
    except aiohttp.ClientError as e:
        print(f"Error: {e}")
    except asyncio.TimeoutError:
        print("Timeout error")
    except Exception as e:
        print(f"Unexpected error: {e}")

# TODO: Example usage
async def main():
    """
    Main function
    """
    # Basic async function
    await async_function()
    
    # Async context manager
    async with AsyncContextManager():
        print("Inside async context")
    
    # Async HTTP client
    urls = [
        'http://example.com',
        'http://example.org',
        'http://example.net'
    ]
    results = await fetch_multiple_urls(urls)
    print(f"Fetched {len(results)} URLs")
    
    # Async file operations
    await write_file('test.txt', 'Hello, World!')
    content = await read_file('test.txt')
    print(f"File content: {content}")
    
    # Async database operations
    db = AsyncDatabase()
    await db.create('key', 'value')
    value = await db.read('key')
    print(f"Database value: {value}")
    
    # Async queue
    queue = AsyncQueue()
    items = [1, 2, 3, 4, 5]
    
    # Start consumer
    consumer_task = asyncio.create_task(consumer(queue))
    
    # Start producer
    await producer(queue, items)
    
    # Wait for queue to be empty
    await queue.join()
    
    # Cancel consumer
    consumer_task.cancel()
    
    # Async logging
    logger = AsyncLogger('app.log')
    logger_task = asyncio.create_task(logger.start())
    
    await logger.log("Test message")
    await asyncio.sleep(0.1)
    
    await logger.stop()
    logger_task.cancel()
    
    # Error handling
    await error_handling()

if __name__ == "__main__":
    asyncio.run(main())

"""
Bài tập về nhà:
1. Tạo một ứng dụng async cho một web scraper
2. Tạo một ứng dụng async cho một file processor
3. Tạo một ứng dụng async cho một database manager
4. Tạo một ứng dụng async cho một message queue
5. Tạo một ứng dụng async cho một logging system
""" 