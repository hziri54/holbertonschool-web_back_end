#!/usr/bin/env python3
"""
A coroutine in this module executes several wait_random calls in parallel.
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Return a list of the delays in ascending order after spawning
    wait_random n times with the given max_delay.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
