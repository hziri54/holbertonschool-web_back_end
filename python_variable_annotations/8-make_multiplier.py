#!/usr/bin/env python3
"""Write a type-annotated function make_multiplier that
takes a float multiplier as argument and returns a function
that multiplies a float by multiplier."""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a number by the given multiplier."""
    
    def multiply(n: float) -> float:
        """Multiplies the input number by the multiplier."""
        return n * multiplier
    
    return multiply
