#!/usr/bin/env python3
"""
The function to return an asyncio task from wait_random
is provided by this module.
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Provide the specified max_delay and return an asyncio task for wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
