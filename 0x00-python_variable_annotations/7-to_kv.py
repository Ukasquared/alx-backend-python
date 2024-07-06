#!/usr/bin/env python3
"""typed module that returns a tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuple"""
    data = (k, v * v)
    return tuple(data)
