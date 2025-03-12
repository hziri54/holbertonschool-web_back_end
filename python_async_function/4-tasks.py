#!/usr/bin/env python3
"""Create an async function that executes multiple asyncio tasks.

This module defines task_wait_n, which runs multiple instances of
wait_random concurrently using task_wait_random.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Run task_wait_random n times and return a list of delays.
    
    Args:
        n (int): Number of tasks to spawn.
        max_delay (int): Maximum delay for each task.
    
    Returns:
        List[float]: List of delay values in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]
    return delays
