#!/usr/bin/env python3
"""This module contains a function `floor` that returns the floor of a float."""

import math


def floor(n: float) -> int:
    """Return the floor of a float.

    Args:
        n (float): The number to floor.

    Returns:
        int: The greatest integer less or equal to n.
    """
    return math.floor(n)
