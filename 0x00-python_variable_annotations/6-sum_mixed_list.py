#!/usr/bin/env python3
"""mixed list of complex types"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sum of a list"""
    return float(sum(mxd_lst))
