#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv) - 1
    if (args == 0):
        print(args, "arguments.")
    elif (args == 1):
        print(args, "argument:".format(sys.argv[0]))
        print("1:", sys.argv[1])
    else:
        print(args, "arguments:")
        for j in range(1, args + 1):
            print("{}: {}".format(j, sys.argv[j]))
