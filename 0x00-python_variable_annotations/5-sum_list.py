#!/usr/bin/env python3
"""sums a float number"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """returns the sum of float numbers"""
    sumlist: float = 0.0
    for value in input_list:
        sumlist += value
    return sumlist
