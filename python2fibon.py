#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://stackoverflow.com/questions/494594/how-to-write-the-fibonacci-sequence-in-python
#  python2fibon.py
#
#  Copyright 2017 mikeh <mikeh@mikeh-desktop>
#
# not yet working ...
#
#
startNumber = int(raw_input("Enter the start number here "))
endNumber = int(raw_input("Enter the end number here "))


def main(args):
#    print map(fib, range(startNumber, endNumber))
    return 0


def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
