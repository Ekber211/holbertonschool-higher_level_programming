#!/usr/bin/python3


def text_indentation(text):
    """Prints text with 2 new lines after '.', '?', and ':'."""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    for char in text:
        result += char
        if char in ".?:":
            result += "\n\n"

    # Split into lines, strip spaces at start/end of each line, then print
    lines = result.split("\n")
    for line in lines:
        if line.strip() != "":
            print(line.strip())
