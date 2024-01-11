#!/usr/bin/env python3
"""complex types"""


def sum_list(input_list: list[float]) -> float:
    """sum of a list"""
    sum: float = 0
    for i in input_list:
        sum += i
    return sum
