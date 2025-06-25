#!/usr/bin/env python3
import asyncio
from typing import List

# Import using dynamic import since filename starts with a number
async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    """Collect 10 random numbers using async comprehension over async_generator."""
    return [i async for i in async_generator()]
