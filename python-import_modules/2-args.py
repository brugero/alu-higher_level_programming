#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    num_args = len(argv) - 1

    if num_args == 0:
        print("argument(s): 0.")
    elif num_args == 1:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("argument(s): {} arguments:".format(num_args))
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
