#!/usr/bin/python3
""" Creating a class that inherits from another class """


class MyList(list):
    """
    MyList class inherits from list class
    """
    def print_sorted(self):
        """
        Functions that prints list in sorted ascending order
        """
        print(sorted(self))
