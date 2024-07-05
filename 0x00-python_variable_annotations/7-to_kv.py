#!/usr/bin/env python3
"""typed module that returns a tuple"""


def to_kv(k: str, v: int | float) -> tuple[str, float):
    """returns a tuple"""
    return (k,
