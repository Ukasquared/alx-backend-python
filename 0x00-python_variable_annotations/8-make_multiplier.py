#!/usr/bin/env python3
"""module make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """module make_multiplier"""
    def func(x: float) -> float:
        """ module"""
        return x * multiplier
    return func
