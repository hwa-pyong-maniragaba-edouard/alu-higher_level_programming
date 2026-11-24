#!/usr/bin/python3
"""
5-text_indentation module.

Provides a function that prints a text with 2 new lines after each of
the characters ., ? and :
"""


def text_indentation(text):
    """Print text with 2 new lines after each '.', '?' and ':'.
    Raises TypeError if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    lines = []
    line = ""
    for char in text:
        line += char
        if char in ".?:":
            lines.append(line.strip())
            line = ""
    lines.append(line.strip())

    print("\n\n".join(lines), end="")
