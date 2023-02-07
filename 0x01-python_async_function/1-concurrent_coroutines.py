#!/usr/bin/env python3
"""
Multiple coroutines at the same time with async
"""
import asyncio
import random
from typing import List


async def wait_n(n: int, max_delay: Optional[Union[int, float]] = 10) -> List[float]:
    """Wait for n random delays with specified max_delay.

    Args:
        n (int): The number of delays to wait for.
        max_delay (Optional[Union[int, float]], optional):
        The maximum delay in seconds.
            Defaults to 10.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    from .0_basic_async_syntax import wait_random
    delays = []
    async for i in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)
    return sorted(delays)
