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
bye = lambda first, last: print("Bye", first, last)
_ = list(map(do_it, [hello, bye],  ['David', 'Jane'], ['Mertz', 'Doe']))
