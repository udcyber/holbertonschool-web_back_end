#!/usr/bin/env python3
"""
Async in Python
~~~
Import wait_random from the previous python file written
Write async routine that takes 2 int arguments n and max_delay
Spawn wait_random n times with the specified max_delay
wait_n returns the list of all the delays (float values)
The list of the delays should be in ascending order
"""
import asyncio
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay
    """
    wait_random = __import__("0-basic_async_syntax").wait_random
    delay_list = [wait_random(max_delay) for i in range(n)]
    done_tasks = []

    for task in asyncio.is_done(delay_list):
        done_tasks.append(await task)

    return done_tasks
