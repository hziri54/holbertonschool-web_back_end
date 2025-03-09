#!/usr/bin/env python3
"""
Petit module qui récupère 10 nombres aléatoires en mode async.
"""

import asyncio
import typing
from 0-async_generator import async_generator


async def async_comprehension() -> typing.List[float]:
    """
    Récupère 10 nombres aléatoires en utilisant une compréhension async.

    Retourne :
        Une liste de 10 nombres flottants entre 0 et 10.
    """
    return [num async for num in async_generator()]  # On boucle en mode async et on récupère direct les valeurs
