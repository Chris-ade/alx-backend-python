#!/usr/bin/env python3
"""
The basics of async
"""
import asyncio
import random


async def wait_random(max_delay=10):
    """Wait for a random delay between 0 and max_delay.

    Args:
        max_delay (int, optional): The maximum delay in seconds.
            Defaults to 10.

    Returns:
        float: The delay in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
