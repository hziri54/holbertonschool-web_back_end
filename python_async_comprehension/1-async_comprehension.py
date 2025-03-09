#!/usr/bin/env python3
""" 
Module qui exécute plusieurs appels asynchrones à wait_random 
et retourne les délais en ordre croissant, sans utiliser sort().
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Lance n fois wait_random avec max_delay et retourne les délais en ordre croissant.

    Args:
        n (int): Nombre d'exécutions de wait_random.
        max_delay (int): Délai maximum pour wait_random.

    Returns:
        List[float]: Liste des délais obtenus, triés en ordre croissant.
    """
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))

    sorted_delays = []
    while delays:
        min_val = min(delays)
        sorted_delays.append(min_val)
        delays.remove(min_val)
    return sorted_delays
