#!/usr/bin/env python3
"""
A coroutine that returns sorted delays after spawning task_wait_random n times.
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Use the given max_delay to spawn task_wait_randomly n times.
    Give back the delay list in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
