#!/usr/bin/env python3
"""
Async in Python
~~~
Import wait_n into 2-measure_runtime.py
Measure the total execution time for wait_n(n, max_delay)
Return total_time / n
Return a float
"""
import time
import asyncio


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay)
    """

    wait_n = __import__("1-concurrent_coroutines").wait_n

    begin_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    return (end_time - begin_time) / n
