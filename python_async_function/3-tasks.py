#!/usr/bin/env python3
"""This module defines a function that returns an asyncio.Task
to run wait_random concurrently.
"""


import asyncio
from typing import Callable
from basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Return an asyncio.Task that will run wait_random with max_delay.

    Args:
        max_delay (int): The maximum delay to pass to wait_random.

    Returns:
        asyncio.Task: The Task object running wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
