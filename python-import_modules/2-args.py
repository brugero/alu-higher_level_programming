#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    num_args = len(argv) - 1  # Subtract 1 to exclude the script name

    if num_args == 0:
        print("Number of argument(s): 0.")
    elif num_args == 1:
        print("Number of argument(s): 1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("Number of argument(s): {} arguments:".format(num_args))
        for i in range(1, num_args + 1):
            print("{}: {}".format(i, argv[i]))
