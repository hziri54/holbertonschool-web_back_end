#!/usr/bin/env python3
"""
Module qui utilise une compréhension async pour récupérer
10 nombres aléatoires depuis async_generator.
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Récupère 10 nombres aléatoires en utilisant une compréhension async.

    Returns:
        List[float]: Une liste contenant 10 nombres flottants aléatoires.
    """
    return [num async for num in async_generator()]
