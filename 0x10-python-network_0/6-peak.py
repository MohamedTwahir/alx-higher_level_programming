#!/usr/bin/python3
"""Module for find_peak function"""


def find_peak(list_of_integers):
    """Finds peak in unsorted list of integers."""
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
