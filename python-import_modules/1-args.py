#!/usr/bin/python3
import sys


def list_args(*argv):
    argv_length = len(argv[0])-1
    if argv_length == 1:
        print("{} argument:".format(argv_length))
    elif argv_length == 0:
        print("{} arguments.".format(argv_length))
    else:
        print("{} arguments:".format(argv_length))
    for x in range(1, len(argv[0])):
        print("{}: {}".format(x, argv[0][x]))


if __name__ == "__main__":
    cmd_input = []
    for i in range(0, len(sys.argv)):
        cmd_input.append(str(sys.argv[i]))
    list_args(cmd_input)