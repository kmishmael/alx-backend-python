#!/usr/bin/env python3
"""complex types"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''convert key and its value to a tuple of the key and
    the square of its value.
    '''
    return (k, float(v**2))
