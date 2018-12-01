#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 28
        Starting with the number 1 and moving to the right in a
        clockwise direction a 5 by 5 spiral is formed as follows:

            21 22 23 24 25
            20  7  8  9 10
            19  6  1  2 11
            18  5  4  3 12
            17 16 15 14 13

        It can be verified that the sum of the numbers on the diagonals is 101.
        What is the sum of the numbers on the diagonals in a
        1001 by 1001 spiral formed in the same way?
"""
# =============================================================================
# (upper left label is the current label)
#
# SOLUTION: 669171001
#
# STATUS: [ok]
# VERIFIED: [ok]
# EXECUTION TIME: [ok]
# =============================================================================

def euler28(maxRow):
    sumDiag = 1
    for i in range(3,maxRow+1,2):
        upder = i**2
        upizq = upder - (i-1)
        downizq = upizq - (i-1)
        downder = downizq - (i-1)

        sumDiag += upder + upizq + downizq + downder
        #print("Vuelta {}, upder {}, upizq {}, downizq {} downder {} SUMA {}".
        #      format(i, upder, upizq, downizq, downder, sumDiag))

    return sumDiag

if __name__ == "__main__":
    print(euler28(5))
    #101
    print(euler28(1001))
    #669171001
