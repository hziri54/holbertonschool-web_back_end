#!/usr/bin/env python3
"""
A function to determine the average wait_n runtime is included in this module.
"""

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Calculate wait_n(n, max_delay)'s average execution time.
    Divides the total_time by n and returns the result.
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    total_time = end_time - start_time
    return total_time / n
