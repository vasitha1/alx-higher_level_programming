#!/usr/bin/python3

import sys


def main(argv):

    length = len(argv)
    arguments = argv[1:]

    if length == 1:
        print("{} arguments.".format(length - 1))

    elif length == 2:
        print("{0} argument:\n{1}: {2}".format((length - 1), (length - 1), arguments[0]))

    else:
        print("{} arguments:".format(length - 1))
        for arg_num in range(length - 1):
            print("{0}: {1}".format((arg_num + 1), arguments[arg_num]))


if __name__ == "__main__":
    main(sys.argv)
