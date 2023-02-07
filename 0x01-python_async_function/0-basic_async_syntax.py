#!/usr/bin/env python3
"""
The basics of async
"""
import asyncio
import random
from typing import Optional, Union


async def wait_random(max_delay: Optional[Union[int, float]] = 10) -> float:
    """Wait for a random delay between 0 and max_delay.

    Args:
        max_delay (Optional[Union[int, float]], optional):
        The max delay in secs. Defaults to 10.

    Returns:
        float: The delay in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
