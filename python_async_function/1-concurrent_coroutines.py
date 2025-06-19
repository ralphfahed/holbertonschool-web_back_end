#!/usr/bin/env python3
"""
Concurrent coroutines that spawn wait_random n times
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Async routine that spawns wait_random n times with specified max_delay.
    Returns list of delays in ascending order without using sort().
    """
    # Create n concurrent tasks
    tasks = [wait_random(max_delay) for _ in range(n)]
    
    # Collect results as they complete to maintain ascending order
    delays = []
    for coro in asyncio.as_completed(tasks):
        delay = await coro
        delays.append(delay)
    
    return delays
