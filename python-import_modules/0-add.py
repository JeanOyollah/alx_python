#!/usr/bin/env python3
from add_0 import add
a = 1
b = 2


def main():
    result = add(a, b)
    print("{} + {} = {}".format(a, b, result))


if __name__ == '__main__':
    main()