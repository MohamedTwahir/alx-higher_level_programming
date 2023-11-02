#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = len(sys.argv)
    if (arguments == 0):
        print(arguments, "arguments.")
    elif (arguments == 1):
        print(arguments, "argument:".format(sys.argv[0]))
        print("1:", sys.argv[1])
    else:
        print(argc, "arguments:")
        for j in range(1, arguments + 1):
            print("{}: {}".format(j, sys.argv[j]))
