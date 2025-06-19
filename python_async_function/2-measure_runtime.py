#!/usr/bin/env python3
"""Module to measure the average runtime of wait_n using time module."""

import time
import asyncio
from concurrent_coroutines import wait_n  # ✅ make sure the filename is valid!

def measure_time(n: int, max_delay: int) -> float:
    """Measure the average time taken by wait_n(n, max_delay).

    Args:
        n (int): Number of times to run wait_random concurrently
        max_delay (int): Maximum delay for wait_random

    Returns:
        float: total execution time divided by n
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()

    total_time = end - start
    return total_time / n
