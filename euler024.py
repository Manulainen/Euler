#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 24
        A permutation is an ordered arrangement of objects.
        For example, 3124 is one possible permutation of the
        digits 1, 2, 3 and 4. If all of the permutations are listed
        numerically or alphabetically, we call it lexicographic order.
        The lexicographic permutations of 0, 1 and 2 are:
        012   021   102   120   201   210

        What is the millionth lexicographic permutation of the
        digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
# =============================================================================
# (upper left label is the current label)
#
# SOLUTION: 2783915460
#
# STATUS: [ok]
# VERIFIED: [ok]
# EXECUTION TIME: [ok]
# =============================================================================

from itertools import permutations

def euler24():
    permutaciones = permutations("0123456789", 10)
    for indice, permu in enumerate(permutaciones, 1):
        if indice == 1000000:
            return int("".join(list(permu)))

if __name__ == "__main__":
    print(euler24())
    #2783915460
