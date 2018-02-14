#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  lambda1.py
#	20.06.2017 03:16:17
#  Copyright 2017 Michael Hewitt <mikeh@electroteach.com>
#
#


def hello1(name):
    print("Hello", name)


hello1('David')

do_it = lambda f, *args: f(*args)

hello = lambda first, last: print("Hello", first, last)

bye = lambda first, last: print("Bye", first, last)
_ = list(map(do_it, [hello, bye],  ['David', 'Jane'], ['Mertz', 'Doe']))

do_all_funcs = lambda fns, *args: [list(map(fn, *args)) for fn in fns]
_ = do_all_funcs([hello, bye], ['David', 'Jane'], ['Mertz', 'Doe'])

hello2 = lambda name: print("Hello", name)
