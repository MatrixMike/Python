#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  primes.py
#
#  Copyright 2017 Michael Hewitt <mikeh@electroteach.com>
#


def get_primes():

    "Simple lazy Sieve of Eratosthenes"
    candidate = 2
    found = []
    while True:
        if all(candidate % prime != 0 for prime in found):
            yield candidate
            found.append(candidate)
        candidate += 1

primes = get_primes()
print(next(primes), next(primes), next(primes))
print(next(primes))

for _, prime in zip(range(10), primes):
    print(prime)
# for _, prime in zip(range(10), primes):
#     print(prime)
