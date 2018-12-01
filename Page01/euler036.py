#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 36
        The decimal number, 585 = b1001001001 (binary),
        is palindromic in both bases.
        Find the sum of all numbers, less than one million,
        which are palindromic in base 10 and base 2.
        (Please note that the palindromic number, in either base,
        may not include leading zeros.)
"""
# =============================================================================
# (upper left label is the current label)
#
# SOLUTION: 872187
#
# STATUS: [ok]
# VERIFIED: [ok]
# EXECUTION TIME: [ok]
# =============================================================================

def euler36(top):

    total_sum = 0
    for i in range(1,top+1):
        if str(i) == str(i)[::-1] and bin(i)[2:] == bin(i)[:1:-1]:
            #print(i)
            total_sum += i
    return total_sum

if __name__ == "__main__":
    print(euler36(1000000))
    # 872187
