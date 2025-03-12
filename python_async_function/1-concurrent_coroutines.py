#!/usr/bin/env python3
"""Execute multiple coroutines concurrently using async.

This module imports the wait_random function from a previous file and
defines an async function called wait_n. The function spawns wait_random 
n times with the specified max_delay and returns a list of the delays 
in ascending order.
"""

import asyncio
from typing import List
wait_r = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Run wait_random n times and return a list of the delays.

    Args:
        n (int): Number of times to call wait_random.
        max_delay (int): Maximum delay value for wait_random.

    Returns:
        List[float]: List of delay values in ascending order.
    """
    tasks = [asyncio.create_task(wait_r(max_delay)) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]
    return delays
