#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 16
        2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
        What is the sum of the digits of the number 2^1000?
"""
# =============================================================================
# (upper left label is the current label)
#
# SOLUTION: 1366
#
# STATUS: [ok]
# VERIFIED: [ok]
# EXECUTION TIME: [ok]
# =============================================================================

def euler16(power):
    return sum([int(x) for x in list(str(2**power))])


if __name__ == "__main__":
    print(euler16(15))
    #26
    print(euler16(1000))
    #1366
