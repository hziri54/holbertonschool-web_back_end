#!/usr/bin/env python3
"""
Ce module contient une coroutine asynchrone qui génère
des nombres aléatoires entre 0 et 10 avec une pause d'une seconde.
"""

import asyncio
import random


async def async_generator() -> typing.Generator[float, None, None]:
    """
    Générateur asynchrone qui attend 1 seconde entre chaque itération
    et retourne un nombre flottant aléatoire entre 0 et 10.

    Retourne :
        typing.Generator[float, None, None] : Un générateur asynchrone de nombres aléatoires.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
