#!/usr/bin/env python3
"""
A coroutine that loops 10 times
Each time asynchronously wait 1 second
Then yield a random number between 0 and 10
"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Generator that returns a float n times.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
