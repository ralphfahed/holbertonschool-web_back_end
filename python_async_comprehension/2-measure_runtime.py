#!/usr/bin/env python3
import asyncio
import time

# Import the async_comprehension coroutine from the previous file
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """Run async_comprehension 4 times in parallel and measure total runtime."""
    start_time = time.perf_counter()

    # Run 4 async_comprehension coroutines in parallel
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )

    end_time = time.perf_counter()
    return end_time - start_time
