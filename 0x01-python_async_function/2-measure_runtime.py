#!/usr/bin/env python3
""" Measure the runtime """
import time
import asyncio
from typing import List


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(max_delay: int = 10, n: int = 0) -> float:
    """
    float measure time
    """
    started = time.perf_counter()
    asyncio.run(wait_n(max_delay, n))
    second = time.perf_counter() - started
    count = second / n

    return count
