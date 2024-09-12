#!/usr/bin/python3

import sys


def main(argv):

    length = len(argv)
    arguments = argv[1:]
    total = 0

    for arg_index in range(length - 1):

        total += int(arguments[arg_index])
    print("{}".format(total))


if __name__ == "__main__":
    main(sys.argv)
