#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        indx = 0
        for i in range(x):
            print(my_list[i], end="")
            indx += 1
            for x in range(indx):
                print("", end="")
        print()
        return indx
    except IndexError:
        print()
        return indx
