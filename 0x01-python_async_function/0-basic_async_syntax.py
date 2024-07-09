#!usr/bin/env python
""" async module """
import asyncio
import random

async def wait_random(max_delay:int = 10) -> float:
    """ basic async module """
    delay:float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
