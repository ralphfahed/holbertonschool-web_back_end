#!/usr/bin/env python3
import asyncio
from typing import List
from 0-async_generator import async_generator  # Import from the previous task


async def async_comprehension() -> List[float]:
    """Collect 10 random numbers using async comprehension over async_generator."""
    return [i async for i in async_generator()]
