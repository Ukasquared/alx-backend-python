#!/usr/bin/env python3
"""sums a float number"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """returns the sum of float numbers"""
    sum_lst: float = 0.0
    for value in mxd_lst:
        sum_lst += value
    return sum_lst
