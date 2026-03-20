#!/usr/bin/python3
"""This module prints text with 2 new lines after '.', '?' and ':'."""


def text_indentation(text):
    """Print text with 2 new lines after '.', '?' and ':'."""

    if type(text) is not str:
        raise TypeError("text must be a string")

    new_line = True

    for char in text:
        if new_line and char == " ":
            continue

        new_line = False
        print(char, end="")

        if char in ".?:":
            print("\n")
            new_line = True
            