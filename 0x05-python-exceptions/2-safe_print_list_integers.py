#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    indx = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            indx += 1
            for x in range(indx):
                print("", end="")
        except TypeError:
            print("", end="")
        except ValueError:
            print("", end="")
    print()
    return indx
