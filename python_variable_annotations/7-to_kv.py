#!/usr/bin/env python3
'''
This module contains the function to_kv which takes a string key and a numeric value (int or float),
and returns a tuple with the key and the square of the value as a float.
'''


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    Returns a tuple where:
    - the first element is the string k,
    - the second element is the square of v as a float.
    '''
    return (k, float(v ** 2))
