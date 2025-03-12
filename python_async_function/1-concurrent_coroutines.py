#!/usr/bin/env python3
"""Measure the execution time of an asynchronous function.

This module imports wait_n from the previous file and defines a function
measure_time that calculates the average execution time of wait_n(n, max_delay).
"""

import time
import asyncio
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    """Calculate the average execution time for wait_n.
    
    Args:
        n (int): Number of coroutines to spawn.
        max_delay (int): Maximum delay for each coroutine.
    
    Returns:
        float: Average execution time per coroutine.
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    
    total_time = end_time - start_time
    return total_time / n
