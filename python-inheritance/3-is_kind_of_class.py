#!/usr/bin/python3
"""Function that checks if an object is an instance of a class or its subclasses."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or a subclass of a_class, otherwise False."""
    return isinstance(obj, a_class)
