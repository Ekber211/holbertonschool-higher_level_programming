#!/usr/bin/python3
"""Class BaseGeometry."""


class BaseGeometry:
    """BaseGeometry class with an unimplemented area method."""

    def area(self):
        """Raise an Exception since area is not implemented."""
        raise Exception("area() is not implemented")
