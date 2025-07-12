"""
Bài tập 7: Xử Lý Bất Đồng Bộ

Mục tiêu:
- Hiểu cách xử lý bất đồng bộ trong Python
- Thực hành với async/await
- Sử dụng asyncio
"""

import asyncio
import time
from datetime import datetime

# TODO: Hàm bất đồng bộ cơ bản
async def say_hello(name, delay):
    """
    Hàm bất đồng bộ đơn giản
    """
    await asyncio.sleep(delay)
    print(f"Xin chào, {name}!")
    return f"Đã chào {name}"

# TODO: Chạy nhiều tác vụ bất đồng bộ
async def run_multiple_tasks():
    """
    Chạy nhiều tác vụ bất đồng bộ cùng lúc
    """
    tasks = [
        say_hello("An", 1),
        say_hello("Bình", 2),
        say_hello("Cường", 3)
    ]
    results = await asyncio.gather(*tasks)
    print("Kết quả:", results)

# Test chạy nhiều tác vụ
print("Test chạy nhiều tác vụ:")
asyncio.run(run_multiple_tasks())

# TODO: Xử lý bất đồng bộ với timeout
async def fetch_data_with_timeout(url, timeout):
    """
    Lấy dữ liệu với timeout
    """
    try:
        async with asyncio.timeout(timeout):
            # Giả lập việc lấy dữ liệu
            await asyncio.sleep(2)
            return f"Dữ liệu từ {url}"
    except asyncio.TimeoutError:
        return f"Timeout khi lấy dữ liệu từ {url}"

# Test timeout
print("\nTest timeout:")
async def test_timeout():
    result1 = await fetch_data_with_timeout("http://example.com", 1)
    result2 = await fetch_data_with_timeout("http://example.com", 3)
    print(result1)
    print(result2)

asyncio.run(test_timeout())

# TODO: Queue bất đồng bộ
async def producer(queue):
    """
    Tạo dữ liệu và đưa vào queue
    """
    for i in range(5):
        await queue.put(f"Dữ liệu {i}")
        await asyncio.sleep(0.5)
    await queue.put(None)  # Tín hiệu kết thúc

async def consumer(queue):
    """
    Lấy và xử lý dữ liệu từ queue
    """
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f"Đã xử lý: {item}")
        queue.task_done()

# Test queue
print("\nTest queue:")
async def test_queue():
    queue = asyncio.Queue()
    await asyncio.gather(
        producer(queue),
        consumer(queue)
    )

asyncio.run(test_queue())

# TODO: Lock bất đồng bộ
class AsyncCounter:
    """
    Counter với lock bất đồng bộ
    """
    def __init__(self):
        self.value = 0
        self.lock = asyncio.Lock()
    
    async def increment(self):
        async with self.lock:
            current = self.value
            await asyncio.sleep(0.1)  # Giả lập xử lý
            self.value = current + 1
            return self.value

# Test lock
print("\nTest lock:")
async def test_lock():
    counter = AsyncCounter()
    tasks = [counter.increment() for _ in range(10)]
    results = await asyncio.gather(*tasks)
    print("Kết quả:", results)

asyncio.run(test_lock())

# TODO: Event bất đồng bộ
async def waiter(event):
    """
    Đợi event được set
    """
    print("Đang đợi event...")
    await event.wait()
    print("Event đã được set!")

async def setter(event):
    """
    Set event sau một khoảng thời gian
    """
    await asyncio.sleep(2)
    print("Setting event...")
    event.set()

# Test event
print("\nTest event:")
async def test_event():
    event = asyncio.Event()
    await asyncio.gather(
        waiter(event),
        setter(event)
    )

asyncio.run(test_event())

"""
Bài tập về nhà:
1. Tạo một hệ thống crawl dữ liệu bất đồng bộ
2. Tạo một server chat bất đồng bộ
3. Tạo một hệ thống xử lý file bất đồng bộ
4. Tạo một pool worker bất đồng bộ
5. Tạo một hệ thống cache bất đồng bộ
""" 