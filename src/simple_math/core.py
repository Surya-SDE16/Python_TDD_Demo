
"""
Core math utilities for TDD practice.

All functions use basic `float` types only.
"""

from typing import List

def add(x: float, y: float) -> float:
    """
    Return the sum of two numbers.

    Examples:
        >>> add(1.5, 2.5)
        4.0
        >>> add(-3.0, 1.0)
        -2.0
    """
    return x+y


def safe_divide(x: float, y: float) -> float:
    """
    Divide `a` by `b`. Raise ValueError when `b` is zero.

    Examples:
        >>> safe_divide(6.0, 3.0)
        2.0
        >>> safe_divide(1.0, 0.0)
        Traceback (most recent call last):
            ...
        ValueError: denominator must not be zero
    """
    if (y == 0):
      raise ValueError("denominator must not be zero") 
    return x/y

def average(ps: List[float]) -> float:
    """
    Compute the arithmetic mean of a non-empty list of floats.

    Examples:
        >>> average([1.0, 3.0, 5.0])
        3.0
        >>> average([])
        Traceback (most recent call last):
            ...
        ValueError: xs must not be empty
    """
    if (ps ==[]):
        raise ValueError("xs must not be empty")
    return(sum(ps)/len(ps))
