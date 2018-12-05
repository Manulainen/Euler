#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 056
        A googol (10^100) is a massive number:
        one followed by one-hundred zeros;
        100^100 is almost unimaginably large:
        one followed by two-hundred zeros.

        Despite their size, the sum of the digits in each number is only 1.

        Considering natural numbers of the form, ab, where a, b < 100,
        what is the maximum digital sum?
"""
# =============================================================================
# (upper left label is the current label)
#
# SOLUTION: 972
#
# STATUS: [ok]
# VERIFIED: [no/ok]
# EXECUTION TIME: [ok]
# =============================================================================

# Remove if not necessary
# import sys
# sys.path.append('../../')
# from Euler.EulerUtils import eulerFunctions as ef

def euler056():
    sumaTotal=0
    for a in range(1,100):
        for b in range(1,100):
            suma = sum([int(x) for x in list(str(a**b))])
            if suma > sumaTotal:
                sumaTotal=suma
    return sumaTotal


if __name__ == "__main__":
    print(euler056())
    # 972
