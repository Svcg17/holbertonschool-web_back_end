#!/usr/bin/env python3
"""Async basics in Python task 1"""
import asyncio
import random
from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(max_delay: float, n: int) -> List[float]:
    """Returns a list of delayed float values using wait_random coroutine"""
    delays: List[float] = []
    for _ in range(n):
        d = await wait_random(max_delay)
        delays.append(d)
    return delays
