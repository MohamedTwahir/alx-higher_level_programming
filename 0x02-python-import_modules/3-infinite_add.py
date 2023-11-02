#!/usr/bin/python3
if __name__ == "__main__":
    import sys, math
    arg_len = len(sys.argv)
    argument = sys.argv
    result = 0

    for i in range(1, arg_len):
        result += int(argument[i])

    print(result)
