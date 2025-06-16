#!/usr/bin/env python3
"""This module contains a function to sum a list of integers and floats."""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of a list of integers and floats as a float.

    Args:
        mxd_lst (List[Union[int, float]]): List containing ints and floats.

    Returns:
        float: The sum of all elements as a float.
    """
    return float(sum(mxd_lst))
