"""
Bài tập 34: Performance

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
from functools import lru_cache
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# TODO: Basic profiling
def basic_profiling():
    """
    Basic profiling example.
    """
    def slow_function():
        time.sleep(1)
        return 42
    
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
    def memory_intensive():
        a = [i for i in range(1000000)]
        b = [i * 2 for i in a]
        c = [i + 1 for i in b]
        return sum(c)
    
    return memory_intensive()

# TODO: CPU profiling
def cpu_profiling():
    """
    CPU profiling example.
    """
    def cpu_intensive():
        result = 0
        for i in range(1000000):
            result += i * i
        return result
    
    profiler = cProfile.Profile()
    profiler.enable()
    result = cpu_intensive()
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
        'percent': process.memory_percent()
    }

# TODO: CPU usage
def cpu_usage():
    """
    CPU usage example.
    """
    process = psutil.Process(os.getpid())
    return {
        'percent': process.cpu_percent(interval=1),
        'num_threads': process.num_threads(),
        'cpu_times': process.cpu_times()
    }

# TODO: Disk usage
def disk_usage():
    """
    Disk usage example.
    """
    return {
        'total': psutil.disk_usage('/').total / 1024 / 1024 / 1024,  # GB
        'used': psutil.disk_usage('/').used / 1024 / 1024 / 1024,    # GB
        'free': psutil.disk_usage('/').free / 1024 / 1024 / 1024,    # GB
        'percent': psutil.disk_usage('/').percent
    }

# TODO: Network usage
def network_usage():
    """
    Network usage example.
    """
    net_io = psutil.net_io_counters()
    return {
        'bytes_sent': net_io.bytes_sent / 1024 / 1024,      # MB
        'bytes_recv': net_io.bytes_recv / 1024 / 1024,      # MB
        'packets_sent': net_io.packets_sent,
        'packets_recv': net_io.packets_recv
    }

# TODO: Performance optimization
def performance_optimization():
    """
    Performance optimization examples.
    """
    # List comprehension vs for loop
    def list_comprehension():
        return [i * 2 for i in range(1000)]
    
    def for_loop():
        result = []
        for i in range(1000):
            result.append(i * 2)
        return result
    
    # Generator vs list
    def generator():
        return (i * 2 for i in range(1000))
    
    def list_creation():
        return [i * 2 for i in range(1000)]
    
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
        return {i: i * 2 for i in range(1000)}
    
    def dict_creation():
        result = {}
        for i in range(1000):
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
    NumPy optimization examples.
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
        'numpy_filtering': numpy_filtering()
    }

# TODO: Caching
def caching():
    """
    Caching examples.
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
        'factorial': factorial(10)
    }

# TODO: Parallel processing
def parallel_processing():
    """
    Parallel processing examples.
    """
    def cpu_bound_task(n):
        return sum(i * i for i in range(n))
    
    def io_bound_task(n):
        time.sleep(0.1)
        return n * n
    
    # Thread pool
    with ThreadPoolExecutor(max_workers=4) as executor:
        thread_results = list(executor.map(io_bound_task, range(10)))
    
    # Process pool
    with ProcessPoolExecutor(max_workers=4) as executor:
        process_results = list(executor.map(cpu_bound_task, range(10)))
    
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