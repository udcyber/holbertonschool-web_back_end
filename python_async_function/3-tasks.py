#!/usr/bin/env python3
"""
Async in Python
~~~
Import wait_random from 0-basic_async_syntax
Function task_wait_random takes an integer max_delay and
returns asyncio.Task.
"""
import asyncio


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Wait random.
    """
    wait_random = __import__("0-basic_async_syntax").wait_random

    return asyncio.create_task(wait_random(max_delay))
