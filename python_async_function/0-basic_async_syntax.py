#!/usr/bin/env python3
"""
An asynchronous function in this module awaits a random delay.

wait_random(max_delay) is a function that asynchron waits for a random
amount of time between 0 and max_delay.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Return the delay after waiting for a random delay up to max_delay seconds."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
