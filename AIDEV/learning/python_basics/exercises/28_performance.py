"""
Bài tập 28: Performance

Mục tiêu:
- Hiểu cách tối ưu hiệu năng trong Python
- Thực hành với profiling và benchmarking
- Sử dụng performance tools
"""

import os
import sys
import time
import cProfile
import pstats
import line_profiler
import memory_profiler
import psutil
import numpy as np
from typing import Any, Dict, List, Optional, Tuple
from datetime import datetime
import json
import re

# TODO: Basic profiling
def basic_profiling():
    """
    Basic profiling example.
    """
    def slow_function():
        time.sleep(1)
        return "Done"
    
    profiler = cProfile.Profile()
    profiler.enable()
    result = slow_function()
    profiler.disable()
    stats = pstats.Stats(profiler)
    stats.sort_stats('cumulative')
    stats.print_stats()
    return result

# TODO: Line profiling
def line_profiling():
    """
    Line profiling example.
    """
    @line_profiler.profile
    def process_data(data: List[int]) -> List[int]:
        result = []
        for item in data:
            result.append(item * 2)
        return result
    
    data = list(range(1000))
    result = process_data(data)
    return result

# TODO: Memory profiling
def memory_profiling():
    """
    Memory profiling example.
    """
    @memory_profiler.profile
    def create_large_list():
        return [i for i in range(1000000)]
    
    result = create_large_list()
    return result

# TODO: CPU profiling
def cpu_profiling():
    """
    CPU profiling example.
    """
    def cpu_intensive():
        result = 0
        for i in range(1000000):
            result += i
        return result
    
    profiler = cProfile.Profile()
    profiler.enable()
    result = cpu_intensive()
    profiler.disable()
    stats = pstats.Stats(profiler)
    stats.sort_stats('cumulative')
    stats.print_stats()
    return result

# TODO: Memory usage
def memory_usage():
    """
    Memory usage example.
    """
    process = psutil.Process()
    memory_info = process.memory_info()
    return {
        'rss': memory_info.rss,
        'vms': memory_info.vms,
        'percent': process.memory_percent()
    }

# TODO: CPU usage
def cpu_usage():
    """
    CPU usage example.
    """
    return {
        'percent': psutil.cpu_percent(),
        'count': psutil.cpu_count(),
        'freq': psutil.cpu_freq()
    }

# TODO: Disk usage
def disk_usage():
    """
    Disk usage example.
    """
    return {
        'total': psutil.disk_usage('/').total,
        'used': psutil.disk_usage('/').used,
        'free': psutil.disk_usage('/').free,
        'percent': psutil.disk_usage('/').percent
    }

# TODO: Network usage
def network_usage():
    """
    Network usage example.
    """
    net_io = psutil.net_io_counters()
    return {
        'bytes_sent': net_io.bytes_sent,
        'bytes_recv': net_io.bytes_recv,
        'packets_sent': net_io.packets_sent,
        'packets_recv': net_io.packets_recv
    }

# TODO: Performance optimization
def performance_optimization():
    """
    Performance optimization example.
    """
    # List comprehension vs for loop
    def list_comprehension():
        return [i * 2 for i in range(1000000)]
    
    def for_loop():
        result = []
        for i in range(1000000):
            result.append(i * 2)
        return result
    
    # Generator vs list
    def generator():
        return (i * 2 for i in range(1000000))
    
    def list_creation():
        return [i * 2 for i in range(1000000)]
    
    # String concatenation
    def string_concatenation():
        result = ""
        for i in range(1000):
            result += str(i)
        return result
    
    def string_join():
        return "".join(str(i) for i in range(1000))
    
    # Dictionary comprehension
    def dict_comprehension():
        return {i: i * 2 for i in range(1000000)}
    
    def dict_creation():
        result = {}
        for i in range(1000000):
            result[i] = i * 2
        return result
    
    return {
        'list_comprehension': list_comprehension(),
        'for_loop': for_loop(),
        'generator': list(generator()),
        'list_creation': list_creation(),
        'string_concatenation': string_concatenation(),
        'string_join': string_join(),
        'dict_comprehension': dict_comprehension(),
        'dict_creation': dict_creation()
    }

# TODO: NumPy optimization
def numpy_optimization():
    """
    NumPy optimization example.
    """
    # Array creation
    def array_creation():
        return np.array([i for i in range(1000000)])
    
    def numpy_arange():
        return np.arange(1000000)
    
    # Array operations
    def array_operations():
        arr = np.array([i for i in range(1000000)])
        return arr * 2
    
    def numpy_operations():
        arr = np.arange(1000000)
        return arr * 2
    
    # Array filtering
    def array_filtering():
        arr = np.array([i for i in range(1000000)])
        return arr[arr > 500000]
    
    def numpy_filtering():
        arr = np.arange(1000000)
        return arr[arr > 500000]
    
    return {
        'array_creation': array_creation(),
        'numpy_arange': numpy_arange(),
        'array_operations': array_operations(),
        'numpy_operations': numpy_operations(),
        'array_filtering': array_filtering(),
        'numpy_filtering': numpy_filtering()
    }

# TODO: Caching
def caching():
    """
    Caching example.
    """
    cache = {}
    
    def fibonacci(n: int) -> int:
        if n in cache:
            return cache[n]
        if n < 2:
            return n
        result = fibonacci(n - 1) + fibonacci(n - 2)
        cache[n] = result
        return result
    
    return fibonacci(10)

# TODO: Parallel processing
def parallel_processing():
    """
    Parallel processing example.
    """
    from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
    
    def process_item(item: int) -> int:
        return item * 2
    
    items = list(range(1000000))
    
    # Thread pool
    with ThreadPoolExecutor() as executor:
        thread_results = list(executor.map(process_item, items))
    
    # Process pool
    with ProcessPoolExecutor() as executor:
        process_results = list(executor.map(process_item, items))
    
    return {
        'thread_results': thread_results,
        'process_results': process_results
    }

# TODO: Example usage
def example_usage():
    """
    Example usage of performance features.
    """
    # Basic profiling
    print("Basic profiling:")
    basic_profiling()
    
    # Line profiling
    print("\nLine profiling:")
    line_profiling()
    
    # Memory profiling
    print("\nMemory profiling:")
    memory_profiling()
    
    # CPU profiling
    print("\nCPU profiling:")
    cpu_profiling()
    
    # Memory usage
    print("\nMemory usage:")
    print(memory_usage())
    
    # CPU usage
    print("\nCPU usage:")
    print(cpu_usage())
    
    # Disk usage
    print("\nDisk usage:")
    print(disk_usage())
    
    # Network usage
    print("\nNetwork usage:")
    print(network_usage())
    
    # Performance optimization
    print("\nPerformance optimization:")
    performance_optimization()
    
    # NumPy optimization
    print("\nNumPy optimization:")
    numpy_optimization()
    
    # Caching
    print("\nCaching:")
    print(caching())
    
    # Parallel processing
    print("\nParallel processing:")
    parallel_processing()

if __name__ == "__main__":
    example_usage()

"""
Bài tập về nhà:
1. Tối ưu hiệu năng cho một ứng dụng FastAPI
2. Tối ưu hiệu năng cho một ứng dụng machine learning
3. Tối ưu hiệu năng cho một hệ thống microservices
4. Tối ưu hiệu năng cho một ứng dụng web với Nginx
5. Tối ưu hiệu năng cho một hệ thống database
""" 