#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 053
        There are exactly ten ways of selecting three from five, 12345:
            123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

        In combinatorics, we use the notation, 5C3 = 10.
        In general,

                  n!
        nCr = ---------, where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
              r!(n−r)!


        It is not until n = 23,
        that a value exceeds one-million: 23C10 = 1144066.

        How many, not necessarily distinct, values of  nCr,
        for 1 ≤ n ≤ 100, are greater than one-million?
"""
# =============================================================================
# (upper left label is the current label)
#
# SOLUTION: 4075
#
# STATUS: [ok]
# VERIFIED: [no/ok]
# EXECUTION TIME: [ok]
# =============================================================================

import sys
sys.path.append('../')
sys.path.append('../../')
from Euler.EulerUtils import eulerFunctions as ef

# bastante trivial los Cnr van de 1 a 100, en total 10000 iteraciones,
# muy faisable. para cada una de ellas se comprubea si es mayor que 1M y
# se aumenta un contador .Quitar los 100 y los 1M

def euler053():
    count = 0
    for n in range(100 + 1):
        for r in range(1,n + 1):
            num = ef.b(n,r)
            if num >= 1000000:
                count += 1
               # print("[{}] para n{} r{} num {} ".format(count, n,r, num))
    return count


if __name__ == "__main__":
    print(euler053())
    # 4075
