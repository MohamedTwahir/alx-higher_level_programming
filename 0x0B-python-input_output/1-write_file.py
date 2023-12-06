#!/usr/bin/python3
""" Creating a function that write a string to a text file """


def write_file(filename="", text=""):
    """
    Function that writes a string to a text file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
