#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 052
        It can be seen that the number, 125874, and its double, 251748,
        contain exactly the same digits, but in a different order.

        Find the smallest positive integer, x,
        such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""
# =============================================================================
# (upper left label is the current label)
#
# SOLUTION: 142857
#
# STATUS: [ok]
# VERIFIED: [ok]
# EXECUTION TIME: [ok]
# =============================================================================

def euler052():
    found = False
    x = 0
    while found is False:
       x += 1
       X = sorted(str(x))
       X6 = sorted(str(x * 6))
       if X == X6:
           X5 = sorted(str(x * 5))
           if X == X5:
               X4 = sorted(str(x * 4))
               if X == X4:
                   X3 = sorted(str(x * 3))
                   if X == X3:
                       X2 = sorted(str(x * 2))
                       if X == X2:
                           found = True
                           return x


if __name__ == "__main__":
    print(euler052())
    # 142857
