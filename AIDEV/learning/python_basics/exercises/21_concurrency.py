"""
Bài tập 21: Concurrency

Mục tiêu:
- Hiểu cách xử lý đồng thời trong Python
- Thực hành với threads và processes
- Sử dụng async/await
"""

import asyncio
import threading
import multiprocessing
import queue
import time
from typing import Any, Callable, Dict, List, Optional, TypeVar
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import random

# TODO: Threading
def thread_function(name: str, delay: float):
    """
    Function to run in a thread
    """
    print(f"Thread {name} starting")
    time.sleep(delay)
    print(f"Thread {name} finishing")

def threading_example():
    """
    Example of threading
    """
    threads = []
    for i in range(3):
        thread = threading.Thread(
            target=thread_function,
            args=(f"Thread-{i}", random.random())
        )
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

# TODO: Thread pool
def thread_pool_example():
    """
    Example of thread pool
    """
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = []
        for i in range(5):
            future = executor.submit(
                thread_function,
                f"Thread-{i}",
                random.random()
            )
            futures.append(future)
        
        for future in futures:
            future.result()

# TODO: Process pool
def process_function(name: str, delay: float):
    """
    Function to run in a process
    """
    print(f"Process {name} starting")
    time.sleep(delay)
    print(f"Process {name} finishing")

def process_pool_example():
    """
    Example of process pool
    """
    with ProcessPoolExecutor(max_workers=3) as executor:
        futures = []
        for i in range(5):
            future = executor.submit(
                process_function,
                f"Process-{i}",
                random.random()
            )
            futures.append(future)
        
        for future in futures:
            future.result()

# TODO: Async/await
async def async_function(name: str, delay: float):
    """
    Async function
    """
    print(f"Async {name} starting")
    await asyncio.sleep(delay)
    print(f"Async {name} finishing")

async def async_example():
    """
    Example of async/await
    """
    tasks = []
    for i in range(5):
        task = asyncio.create_task(
            async_function(f"Task-{i}", random.random())
        )
        tasks.append(task)
    
    await asyncio.gather(*tasks)

# TODO: Thread-safe queue
class ThreadSafeQueue:
    """
    Thread-safe queue implementation
    """
    def __init__(self):
        self.queue = queue.Queue()
    
    def put(self, item: Any):
        """
        Put item in queue
        """
        self.queue.put(item)
    
    def get(self) -> Any:
        """
        Get item from queue
        """
        return self.queue.get()
    
    def empty(self) -> bool:
        """
        Check if queue is empty
        """
        return self.queue.empty()

# TODO: Producer-consumer
def producer(queue: ThreadSafeQueue, items: List[Any]):
    """
    Producer function
    """
    for item in items:
        print(f"Producing {item}")
        queue.put(item)
        time.sleep(random.random())

def consumer(queue: ThreadSafeQueue):
    """
    Consumer function
    """
    while True:
        try:
            item = queue.get(timeout=1)
            print(f"Consuming {item}")
            time.sleep(random.random())
        except queue.Empty:
            break

def producer_consumer_example():
    """
    Example of producer-consumer pattern
    """
    queue = ThreadSafeQueue()
    items = list(range(5))
    
    producer_thread = threading.Thread(
        target=producer,
        args=(queue, items)
    )
    consumer_thread = threading.Thread(
        target=consumer,
        args=(queue,)
    )
    
    producer_thread.start()
    consumer_thread.start()
    
    producer_thread.join()
    consumer_thread.join()

# TODO: Async producer-consumer
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
    
    def empty(self) -> bool:
        """
        Check if queue is empty
        """
        return self.queue.empty()

async def async_producer(queue: AsyncQueue, items: List[Any]):
    """
    Async producer function
    """
    for item in items:
        print(f"Producing {item}")
        await queue.put(item)
        await asyncio.sleep(random.random())

async def async_consumer(queue: AsyncQueue):
    """
    Async consumer function
    """
    while True:
        try:
            item = await queue.get()
            print(f"Consuming {item}")
            await asyncio.sleep(random.random())
        except asyncio.QueueEmpty:
            break

async def async_producer_consumer_example():
    """
    Example of async producer-consumer pattern
    """
    queue = AsyncQueue()
    items = list(range(5))
    
    producer_task = asyncio.create_task(
        async_producer(queue, items)
    )
    consumer_task = asyncio.create_task(
        async_consumer(queue)
    )
    
    await asyncio.gather(producer_task, consumer_task)

# TODO: Example usage
def example_usage():
    """
    Example usage of concurrency
    """
    # Threading example
    print("Threading example:")
    threading_example()
    
    # Thread pool example
    print("\nThread pool example:")
    thread_pool_example()
    
    # Process pool example
    print("\nProcess pool example:")
    process_pool_example()
    
    # Async/await example
    print("\nAsync/await example:")
    asyncio.run(async_example())
    
    # Producer-consumer example
    print("\nProducer-consumer example:")
    producer_consumer_example()
    
    # Async producer-consumer example
    print("\nAsync producer-consumer example:")
    asyncio.run(async_producer_consumer_example())

if __name__ == "__main__":
    example_usage()

"""
Bài tập về nhà:
1. Tạo một hệ thống xử lý đồng thời cho một ứng dụng FastAPI
2. Tạo một hệ thống xử lý đồng thời cho một ứng dụng machine learning
3. Tạo một hệ thống xử lý đồng thời cho một hệ thống microservices
4. Tạo một hệ thống xử lý đồng thời cho một ứng dụng web với Nginx
5. Tạo một hệ thống xử lý đồng thời cho một hệ thống database
""" 