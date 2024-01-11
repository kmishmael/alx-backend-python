#!/usr/bin/env python3
"""mixed list of complex types"""
from typing import List


def sum_mixed_list(mxd_list: List[float | int]) -> float:
    """sum of a list"""
    sum: float = 0
    for i in mxd_list:
        sum += i
    return sum