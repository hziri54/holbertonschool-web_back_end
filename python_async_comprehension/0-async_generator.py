#!/usr/bin/env python3
import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """
    Boucle 10 fois, attend 1 seconde de manière asynchrone,
    puis génère un nombre aléatoire entre 0 et 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
