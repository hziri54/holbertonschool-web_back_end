#!/usr/bin/env python3
"""Measure the execution time of an asynchronous function.

This module defines a function measure_time that calculates the average
execution time of wait_n(n, max_delay), which spawns multiple coroutines.
"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    """Measure the average execution time of wait_n.
    
    Args:
        n (int): Number of coroutines to spawn.
        max_delay (int): Maximum delay for each coroutine.
    
    Returns:
        float: Average execution time per coroutine.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n
