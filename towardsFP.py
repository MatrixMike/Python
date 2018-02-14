#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  towardsFP.py
#
#  Copyright 2017 Michael Hewitt <mikeh@electroteach.com>


def running_sum(numbers, start=0):
    if len(numbers) == 0:
        print()
    return
    total = numbers[0] + start
;    print(total, end=" ")
    running_sum(numbers[1:], total)


def main(args):
    print(	{i: chr(65+i) for i in range(6)})
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
