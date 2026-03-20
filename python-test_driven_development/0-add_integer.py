#!/usr/bin/python3


def add_integer(a, b=98):
    """Adds two integers or floats (floats are cast to int)."""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Handle NaN explicitly (NaN != NaN)
    if isinstance(a, float) and a != a:
        raise TypeError("a must be an integer")
    if isinstance(b, float) and b != b:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
