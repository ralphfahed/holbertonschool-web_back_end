#!/usr/bin/env python3
"""Module that runs task_wait_random concurrently n times
and returns a list of delays in order of completion.
"""

import asyncio
from typing import List
from tasks3 import task_wait_random  # ✅ import from your previous task

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn task_wait_random n times with max_delay concurrently.

    Args:
        n (int): Number of tasks to run
        max_delay (int): Max delay for each task

    Returns:
        List[float]: List of delays in ascending order of completion
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)

    return delays
