"""
Bài tập 40: Performance

Mục tiêu:
- Hiểu cách tối ưu performance trong Python
- Thực hành với profiling và benchmarking
- Sử dụng performance tools
"""

import os
import sys
import time
import pytest
import unittest
import cProfile
import line_profiler
import memory_profiler
import psutil
import numpy as np
from typing import Any, Dict, List, Optional, Tuple
from datetime import datetime
import json
import re
from functools import wraps, lru_cache
from contextlib import contextmanager
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

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
    profiler.print_stats(sort='cumulative')
    
    return result

# TODO: Line profiling
def line_profiling():
    """
    Line profiling example.
    """
    @profile
    def slow_function():
        a = [i for i in range(1000)]
        b = [i * 2 for i in a]
        c = [i + 1 for i in b]
        return sum(c)
    
    return slow_function()

# TODO: Memory profiling
def memory_profiling():
    """
    Memory profiling example.
    """
    @profile
    def memory_intensive_function():
        a = [i for i in range(1000000)]
        b = [i * 2 for i in a]
        c = [i + 1 for i in b]
        return sum(c)
    
    return memory_intensive_function()

# TODO: CPU profiling
def cpu_profiling():
    """
    CPU profiling example.
    """
    def cpu_intensive_function():
        result = 0
        for i in range(1000000):
            result += i * i
        return result
    
    profiler = cProfile.Profile()
    profiler.enable()
    result = cpu_intensive_function()
    profiler.disable()
    profiler.print_stats(sort='cumulative')
    
    return result

# TODO: Memory usage
def memory_usage():
    """
    Memory usage example.
    """
    process = psutil.Process(os.getpid())
    memory_info = process.memory_info()
    
    return {
        'rss': memory_info.rss / 1024 / 1024,  # MB
        'vms': memory_info.vms / 1024 / 1024,  # MB
        'percent': process.memory_percent(),
    }

# TODO: CPU usage
def cpu_usage():
    """
    CPU usage example.
    """
    process = psutil.Process(os.getpid())
    cpu_percent = process.cpu_percent(interval=1)
    cpu_times = process.cpu_times()
    
    return {
        'percent': cpu_percent,
        'user': cpu_times.user,
        'system': cpu_times.system,
        'children_user': cpu_times.children_user,
        'children_system': cpu_times.children_system,
    }

# TODO: Disk usage
def disk_usage():
    """
    Disk usage example.
    """
    disk_usage = psutil.disk_usage('/')
    
    return {
        'total': disk_usage.total / 1024 / 1024 / 1024,  # GB
        'used': disk_usage.used / 1024 / 1024 / 1024,  # GB
        'free': disk_usage.free / 1024 / 1024 / 1024,  # GB
        'percent': disk_usage.percent,
    }

# TODO: Network usage
def network_usage():
    """
    Network usage example.
    """
    net_io = psutil.net_io_counters()
    
    return {
        'bytes_sent': net_io.bytes_sent / 1024 / 1024,  # MB
        'bytes_recv': net_io.bytes_recv / 1024 / 1024,  # MB
        'packets_sent': net_io.packets_sent,
        'packets_recv': net_io.packets_recv,
    }

# TODO: Performance optimization
def performance_optimization():
    """
    Performance optimization example.
    """
    # List comprehension vs for loop
    def list_comprehension():
        return [i * 2 for i in range(1000)]
    
    def for_loop():
        result = []
        for i in range(1000):
            result.append(i * 2)
        return result
    
    # String concatenation vs join
    def string_concatenation():
        result = ""
        for i in range(1000):
            result += str(i)
        return result
    
    def string_join():
        return "".join(str(i) for i in range(1000))
    
    # Dictionary comprehension
    def dict_comprehension():
        return {i: i * 2 for i in range(1000)}
    
    def dict_for_loop():
        result = {}
        for i in range(1000):
            result[i] = i * 2
        return result
    
    return {
        'list_comprehension': list_comprehension(),
        'for_loop': for_loop(),
        'string_concatenation': string_concatenation(),
        'string_join': string_join(),
        'dict_comprehension': dict_comprehension(),
        'dict_for_loop': dict_for_loop(),
    }

# TODO: NumPy optimization
def numpy_optimization():
    """
    NumPy optimization example.
    """
    # Array creation
    def array_creation():
        return np.array([i for i in range(1000)])
    
    def numpy_arange():
        return np.arange(1000)
    
    # Array operations
    def array_operations():
        a = np.array([i for i in range(1000)])
        b = np.array([i * 2 for i in range(1000)])
        return a + b
    
    def numpy_operations():
        a = np.arange(1000)
        b = np.arange(1000) * 2
        return a + b
    
    # Array filtering
    def array_filtering():
        a = np.array([i for i in range(1000)])
        return a[a > 500]
    
    def numpy_filtering():
        a = np.arange(1000)
        return a[a > 500]
    
    return {
        'array_creation': array_creation(),
        'numpy_arange': numpy_arange(),
        'array_operations': array_operations(),
        'numpy_operations': numpy_operations(),
        'array_filtering': array_filtering(),
        'numpy_filtering': numpy_filtering(),
    }

# TODO: Caching
def caching():
    """
    Caching example.
    """
    # Fibonacci with caching
    @lru_cache(maxsize=128)
    def fibonacci(n):
        if n < 2:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)
    
    # Factorial with caching
    @lru_cache(maxsize=128)
    def factorial(n):
        if n < 2:
            return 1
        return n * factorial(n - 1)
    
    return {
        'fibonacci': fibonacci(10),
        'factorial': factorial(10),
    }

# TODO: Parallel processing
def parallel_processing():
    """
    Parallel processing example.
    """
    # I/O-bound task
    def io_bound_task():
        time.sleep(1)
        return "Done"
    
    # CPU-bound task
    def cpu_bound_task(n):
        return sum(i * i for i in range(n))
    
    # Thread pool
    with ThreadPoolExecutor(max_workers=4) as executor:
        thread_results = list(executor.map(io_bound_task, range(4)))
    
    # Process pool
    with ProcessPoolExecutor(max_workers=4) as executor:
        process_results = list(executor.map(cpu_bound_task, [1000000] * 4))
    
    return {
        'thread_results': thread_results,
        'process_results': process_results,
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
    print(performance_optimization())
    
    # NumPy optimization
    print("\nNumPy optimization:")
    print(numpy_optimization())
    
    # Caching
    print("\nCaching:")
    print(caching())
    
    # Parallel processing
    print("\nParallel processing:")
    print(parallel_processing())

if __name__ == "__main__":
    example_usage()

"""
Bài tập về nhà:
1. Tối ưu performance cho một ứng dụng FastAPI
2. Tối ưu performance cho một ứng dụng machine learning
3. Tối ưu performance cho một hệ thống microservices
4. Tối ưu performance cho một ứng dụng web với Nginx
5. Tối ưu performance cho một hệ thống database
""" 