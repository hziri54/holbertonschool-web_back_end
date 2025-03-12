#!/usr/bin/env python3
"""Create a function that returns an asyncio.Task.

This module defines task_wait_random, which takes an integer max_delay and
returns an asyncio Task that executes wait_random.
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """Return an asyncio Task for wait_random with the given max_delay.
    
    Args:
        max_delay (int): The maximum delay for wait_random.
    
    Returns:
        asyncio.Task: A task that runs wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
