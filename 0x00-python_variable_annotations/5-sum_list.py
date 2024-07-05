#!/usr/bin/env python3
"""sums a float number"""


def sum_list(input_list: list[float]) -> float:
   """returns the sum of float numbers"""
   sumlist: float = 0.0
   for value in input_list:
       sumlist += value
   return sumlist
