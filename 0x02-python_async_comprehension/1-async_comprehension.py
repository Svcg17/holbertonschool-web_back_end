#!/usr/bin/env python3
"""Async Comprehension task 1"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """Collects 10 random numbers and returns them"""
    randomNums = [i async for i in async_generator()]
    return randomNums
