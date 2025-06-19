#!/usr/bin/env python3
"""This module defines a coroutine that runs task_wait_random n times
and returns a list of delays in order of completion.
"""

import asyncio
from typing import List
from 3-tasks import task_wait_random  # ✅ Make sure 3-tasks.py is in same folder

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Runs task_wait_random n times and returns delays in order of completion.

    Args:
        n (int): number of times to run task_wait_random
        max_delay (int): max delay passed to each task

    Returns:
        List[float]: list of delays in ascending order of completion
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)

    return delays
