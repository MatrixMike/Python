#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  fibonacci1.py
#
#  Copyright 2017 Michael Hewitt <mikeh@electroteach.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#


from collections.abc import Iterable


class Fibonacci(Iterable):
    def __init__(self):
        self.a, self.b = 0, 1
        self.total = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        self.total += self.a
        return self.a

    def running_sum(self):
        return self.total

fib = Fibonacci()
fib.running_sum()
for _, i in zip(range(10), fib):
    print(i, end = " ")
