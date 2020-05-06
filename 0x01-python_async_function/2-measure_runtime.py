#!/usr/bin/env python3
"""Async basics in Python task 0"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    start = time.perf_counter()
    wait_n(n, max_delay)
    total = time.perf_counter() - start
    return total / n
