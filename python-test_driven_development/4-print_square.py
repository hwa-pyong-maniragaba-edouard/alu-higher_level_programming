#!/usr/bin/python3
"""
4-print_square module.

Provides a function that prints a square with the character #.
"""


def print_square(size):
    """Print a square of size size with the character #.
    Raises TypeError if size is not an integer.
    Raises ValueError if size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
