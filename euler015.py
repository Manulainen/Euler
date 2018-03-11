euler#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 15
        Starting in the top left corner of a 2×2 grid,
        and only being able to move to the right and down,
        there are exactly 6 routes to the bottom right corner.

        How many such routes are there through a 20×20 grid?
"""
# =============================================================================
# [resuelto] 137846528820
# [comprobado]
# =============================================================================

from math import factorial

def comb(a,b):
    return int(factorial(a)/(factorial(b)*factorial(a-b)))

def euler15(grid_length):
    return comb(grid_length * 2, grid_length)


if __name__ == "__main__":
    print(euler15(20))
    #137846528820
