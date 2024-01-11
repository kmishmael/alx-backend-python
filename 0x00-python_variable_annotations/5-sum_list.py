#!/usr/bin/env python3
"""complex types"""
from typing import List

def sum_list(input_list: List[float]) -> float:
    """sum of a list"""
    sum: float = 0
    for i in input_list:
        sum += i
    return sum
