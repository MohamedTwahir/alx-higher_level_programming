#!/usr/bin/python3
def no_c(my_string):
    string = ""
    for elements in my_string:
        if elements != "C" and elements != "c":
            string = string + elements
    return string
