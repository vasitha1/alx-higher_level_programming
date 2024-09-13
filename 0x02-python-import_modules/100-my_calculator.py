#!/usr/bin/python3

from calculator_1 import add, mul, sub, div
from sys import exit, argv


def main(argv):

    length = len(argv)
    operators = {"+": add, "-": sub, "*": mul, "/": div}

    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    else:
        print("{0} {1} {2} = {3}".format(
            argv[1],
            argv[2],
            argv[3],
            operators[argv[2]](int(argv[1]), int(argv[3]))
            ))


if __name__ == "__main__":
    import sys
    main(sys.argv)
