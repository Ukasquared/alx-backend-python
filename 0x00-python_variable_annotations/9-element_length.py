#!/usr/bin/env python3
"""module iterable"""
from typing import List, Iterable, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """module iterable """
    return [(i, len(i)) for i in lst]
