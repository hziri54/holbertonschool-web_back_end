#!/usr/bin/env python3
"""
Module contenant une coroutine asynchrone qui attend un temps aléatoire
avant de le retourner.
"""

import asyncio
import random
from typing import Union


async def wait_random(max_delay: int = 10) -> float:
    """
    Attend un délai aléatoire entre 0 et max_delay secondes, puis retourne ce délai.

    Args:
        max_delay (int, optionnel) : Durée maximale d'attente en secondes (par défaut 10).

    Returns:
        float: Temps d'attente aléatoire généré.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
