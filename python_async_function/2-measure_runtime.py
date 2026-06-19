#!/usr/bin/env python3
"""
Async in Python
~~~
Measure the total execution time for wait_n(n, max_delay)
"""
import time
import asyncio


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay)
    """

    wait_n = __import__("1-concurrent.coroutines").wait_n

    gotime = time.time()
    asyncio.run(wait_n(n, max_delay))
    endtime = time.time()

    return (endtime - gotime) / n
