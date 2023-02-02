#!/usr/bin/env python3
"""
Multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Multiplies a float by multiplier.
    """
    def multiply(n: float) -> float:
        """ multiplies a float by multiplier """
        return n * multiplier
    return multiply
