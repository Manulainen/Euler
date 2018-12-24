#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 058
        Starting with 1 and spiralling anticlockwise in the following way,
        a square spiral with side length 7 is formed.

            37 36 35 34 33 32 31
            38 17 16 15 14 13 30
            39 18  5  4  3 12 29
            40 19  6  1  2 11 28
            41 20  7  8  9 10 27
            42 21 22 23 24 25 26
            43 44 45 46 47 48 49

        It is interesting to note that the odd squares lie along
        the bottom right diagonal, but what is more interesting is that
        8 out of the 13 numbers lying along both diagonals are prime;
        that is, a ratio of 8/13 ≈ 62%.

        If one complete new layer is wrapped around the spiral above,
        a square spiral with side length 9 will be formed.
        If this process is continued, what is the side length of the square
        spiral for which the ratio of primes along
        both diagonals first falls below 10%?
"""
# =============================================================================
# (upper left label is the current label)
#
# SOLUTION: 26241
#
# STATUS: [ok]
# VERIFIED: [ok]
# EXECUTION TIME: [long/ok]
# =============================================================================

# Remove if not necessary
import sys
sys.path.append('../../')
sys.path.append('../')
from Euler.EulerUtils import eulerFunctions as ef

def euler058():
    salto=0
#    A=[]
#    B=[]
#    C=[]
#    D=[]
    numsTotales = 1
    numsPrimos = 0

    ratio = 11 # Un numero mayor de 10... no muy elegante
    length = 1 # Las longitudes van en impares
    while ratio >= 10 :
        length += 2
        salto += 2
        a = length**2
        d = a - salto
        c = d - salto
        b = c - salto

#        A.append(a)
#        D.append(d)
#        C.append(c)
#        B.append(b)

        numsTotales += 4

        if ef.is_prime(a):
            numsPrimos +=1
        if ef.is_prime(b):
            numsPrimos +=1
        if ef.is_prime(c):
            numsPrimos +=1
        if ef.is_prime(d):
            numsPrimos +=1

#        print(A)
#        print(D)
#        print(C)
#        print(B)

        ratio = (numsPrimos/numsTotales)*100
#        print("Longitud {}, Ratio {}".format(length, ratio))
    return length

if __name__ == "__main__":
    print(euler058())
    # 26241
