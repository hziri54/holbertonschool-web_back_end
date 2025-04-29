#!/usr/bin/env python3
"""
Module qui mesure le temps d'exécution de 4 appels en parallèle
à async_comprehension.
"""

import asyncio
import time
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Exécute async_comprehension 4 fois en parallèle et mesure le temps total.

    Returns:
        float: Temps total d'exécution en secondes.
    """
    start_time = time.perf_counter()

    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end_time = time.perf_counter()
    return end_time - start_time
