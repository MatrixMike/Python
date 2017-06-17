#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  lambda1.py
#
#  Copyright 2017 Michael Hewitt <mikeh@electroteach.com>
#
#

do_it = lambda f, *args: f(*args)
hello = lambda first, last: print("Hello", first, last)
do_all_funcs = lambda fns, *args: [list(map(fn, *args)) for fn in fns]
bye = lambda first, last: print("Bye", first, last)
_ = list(map(do_it, [hello, bye],  ['David', 'Jane'], ['Mertz', 'Doe']))
_ = do_all_funcs([hello, bye], ['David', 'Jane'], ['Mertz', 'Doe'])

hello2 = lambda name: print("Hello", name)
hello1('David')
