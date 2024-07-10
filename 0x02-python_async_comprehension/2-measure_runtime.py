#!/usr/bin/env python3
""" measure_runtime coroutine that will
execute async_comprehension four times
in parallel using asyncio.gather"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure the time it takes
    for multiple coroutines to run
    """""

    started = time.perf_counter()
    await asyncio.gather(*([async_comprehension() for i in range(4)]))
    time_taken = time.perf_counter() - started
    return time_taken
