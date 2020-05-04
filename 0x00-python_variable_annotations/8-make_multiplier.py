#!/usr/bin/env python3
"""Basic annotations task 8"""
from typing import Callable
import math


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by another float
    """
    def mult(m):
        return m * multiplier
    return mult

