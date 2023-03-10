#!/usr/bin/env python3
""" Run time for four parallel comprehensions """
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime and return it.
    """
    start = time.perf_counter()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    taking_time = time.perf_counter()

    alls = taking_time - start

    return alls
