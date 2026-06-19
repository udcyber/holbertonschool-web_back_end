#!/usr/bin/env python3
"""
Take the code from wait_n and alter it into a new function task_wait_n
"""
import asyncio
from typing import List

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Alter code from wait_n into task_wait_n.
    """
    task_wait_random = __import__("3-tasks").task_wait_random
    delay_list = [task_wait_random(max_delay) for i in range(n)]
    done_tasks = []

    for task in asyncio.as_completed(delay_list):
        done_tasks.append(await task)

    return done_tasks
