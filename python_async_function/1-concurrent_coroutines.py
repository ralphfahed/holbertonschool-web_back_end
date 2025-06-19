#!/usr/bin/env python3
"""This module defines a coroutine wait_n that runs wait_random n times
concurrently and returns a list of the delays in ascending order
based on completion time.
"""

import asyncio
from typing import List
from 0-basic_async_syntax import wait_random  # Make sure file is renamed

async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times with max_delay.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay to pass to wait_random.

    Returns:
        List[float]: List of delays, in ascending order of completion.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)

    return delays
