#!/usr/bin/python3
"""
This module contains a function that indents text
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print(f"{text[i]}\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        else:
            print(text[i], end="")
        i += 1
