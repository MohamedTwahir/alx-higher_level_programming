#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        divi = a / b
    except (ZeroDivisionError, TypeError) as e:
        divi = None
        print("Inside result: {}".format(divi))
    finally:
        print("Inside result: {}".format(divi))
        return divi
