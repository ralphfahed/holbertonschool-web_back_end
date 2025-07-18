#!/usr/bin/env python3
'''
This module defines make_multiplier function.
'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier 
    Args:
        multiplier (float): The multiplier value.
    Returns:
        Callable[[float], float]: A function that takes a float and
        returns the product.
    """
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
