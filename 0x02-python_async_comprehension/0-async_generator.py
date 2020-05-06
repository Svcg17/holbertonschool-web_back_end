#!/usr/bin/env python3
"""Async Generator task 0"""
import asyncio
import random


async def async_generator():
    """yields a random number between 0 and 10"""
    for _ in range(10):
        await asyncio.sleep(1)
        r = random.uniform(0, 10)
        yield r
