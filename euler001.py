#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 1
        if we list all the natural numbers below 10 that are multiples
        of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
        Find the sum of all the multiples of 3 or 5 below 1000.
"""
# =============================================================================
# (upper left label is the current label)
#
# SOLUTION: 233168
#
# STATUS: [ok]
# VERIFIED:[ok]
# EXECUTION TIME: [ok]
# =============================================================================

def euler1(cota_sup):
    total = 0
    for i in range(cota_sup):
        if i%3 == 0 or i%5 == 0:
            total += i
    return total


if __name__ == "__main__":
    print(euler1(10))
#23
    print(euler1(1000))
#233168
