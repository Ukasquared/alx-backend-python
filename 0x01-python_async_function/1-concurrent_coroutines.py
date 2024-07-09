#!/usr/bin/env python3
""" concurrent routine"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ concurrent routine"""

    delay: List[float] = []
    all_task: List[float] = []

    for i in range(n):
        delay.append(wait_random(max_delay))

    for task in asyncio.as_completed(delay):
        all_task.append(await task)

    return all_task
