#!/usr/bin/env python3
"""This module defines an asynchronous coroutine wait_n that
runs wait_random n times concurrently with a given max_delay,
and returns the list of delays in ascending order of completion.
"""


import asyncio
from typing import List
from basic_async_syntax import wait_random  # Ensure your file is renamed accordingly


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times with max_delay concurrently.

    Args:
        n (int): Number of concurrent calls to wait_random.
        max_delay (int): Maximum delay to be passed to wait_random.

    Returns:
        List[float]: List of delays in ascending order (by completion).
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)

    return delays
