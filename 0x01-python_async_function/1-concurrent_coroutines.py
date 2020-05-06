#!/usr/bin/env python3
"""Async basics in Python task 1"""
import asyncio
import random
from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(max_delay: float, n: int) -> List[float]:
    """Returns a list of delayed float values using wait_random coroutine"""
    delays: List[float] = []
    tasks: List[float] = []

    for _ in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))

    for t in asyncio.as_completed(tasks):
        delays.append(await(t))

    if not delays:
        for _ in range(max_delay):
            delays.append(0.0)

    return delays
