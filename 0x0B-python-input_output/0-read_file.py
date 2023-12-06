#!/usr/bin/python3
"""Creating a function that reads a text file"""


def read_file(filename=""):
    """ a function that reads a file and prints it """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
