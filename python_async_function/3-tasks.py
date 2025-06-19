#!/usr/bin/env python3
"""Module that provides a function to create an asyncio Task
for the wait_random coroutine.
"""

import asyncio
from basic_async_syntax import wait_random  # ✅ ensure the file was renamed!

def task_wait_random(max_delay: int) -> asyncio.Task:
    """Return an asyncio.Task for wait_random with max_delay.

    Args:
        max_delay (int): The maximum delay.

    Returns:
        asyncio.Task: Task object running wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
