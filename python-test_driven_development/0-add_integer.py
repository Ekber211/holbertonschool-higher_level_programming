#!/usr/bin/python3
"""This module contains a function that adds two integers.
It validates input types.
It casts floats to integers.
It raises appropriate exceptions.
"""


def add_integer(a, b=98):
    """Add two integers.
    Returns the result.
    Raises TypeError if invalid.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if a != a:
        raise TypeError("a must be an integer")

    if b != b:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
    