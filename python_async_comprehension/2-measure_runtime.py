#!/usr/bin/env python3
"""
Import async_comprehension
A couroutine that will execute async_comprehension four times
in parallel using asyncio.gather
measure_runtime should measure the total runtime and return it
"""
import time
import asyncio
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Execute async_comprehension four times in parallel.
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end = time.time()

    return end - start
