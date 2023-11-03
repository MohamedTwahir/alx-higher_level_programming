#!/usr/bin/python3

if __name__ == "__main__":
    """
    Built my own basic Calculator

    """
    import sys
    from calculator_1 import add, sub, mul, div

    # Making sure it handles three arguments
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
# Creating a dictionary for the operators needed
    operts = {"+": add, "-": sub, "*": mul, "/": div}
    # making sure the operator assigned in the key value pair is available
    if sys.argv[2] not in list(operts.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} {} {} = {}".format(a, sys.argv[2], b, operts[sys.argv[2]](a, b)))
