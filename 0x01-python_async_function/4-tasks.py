#!/usr/bin/env python3
""" concurrent routine"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ concurrent routine"""

    delay: List[float] = []
    all_task: List[float] = []

    for i in range(n):
        delay.append(task_wait_random(max_delay))

    for task in asyncio.as_completed(delay):
        all_task.append(await task)

    return all_task
