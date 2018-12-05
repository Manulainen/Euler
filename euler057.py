#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 057
        It is possible to show that the square root of two can be expressed
        as an infinite continued fraction.

        √ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

        By expanding this for the first four iterations, we get:

        1 + 1/2 = 3/2 = 1.5
        1 + 1/(2 + 1/2) = 7/5 = 1.4
        1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
        1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

        The next three expansions are 99/70, 239/169, and 577/408,
        but the eighth expansion, 1393/985, is the first example where
        the number of digits in the numerator exceeds the number of digits
        in the denominator.

        In the first one-thousand expansions,how many
        fractions contain a numerator with more digits than denominator?
"""
# =============================================================================
# (upper left label is the current label)
#
# SOLUTION: 157
#
# STATUS: [ok]
# VERIFIED: [no/ok]
# EXECUTION TIME: [long/ok]
# =============================================================================

# Remove if not necessary
# import sys
# sys.path.append('../../')
# from Euler.EulerUtils import eulerFunctions as ef

# El problema es escribir esta funcion.
# raiz = 1 + 1/A
# A = 2
# A = 2 + 1/A


# La primera aproximacion usando una función recursiva revienta la
# pila de python. Hay que hacerlo iterativo.


# Recursivo. Mala aproximacion.
#def A(prof):
#    if prof == 1:
#        return 2
#    else:
#         return 2 + (1/A(prof-1))
#
#def raiz(prof):
#	return 1 + (1/A(prof))


# Segunda aproximacion, Quitando recursion de cola
# prof es el numero de expansiones
#
from fractions import Fraction as frac

def raiz(prof):
    return frac(1 + (1 / A(prof - 1)))

def A(prof):
    if prof == 0:
        return frac(2)
    else:
        a=frac(2 + (1 / 2))
        for i in range(prof - 1):
            a=frac(2 + 1 / a)
        return frac(a)

def euler057(top):
    totalFound = 0
    for i in range(1,top + 1):
        sqrt = raiz(i)
        if len(str(sqrt.numerator)) > len(str(sqrt.denominator)):
            totalFound +=1
        #print(i, sqrt)
    return totalFound


if __name__ == "__main__":
    print(euler057(8))
    # 1
    print(euler057(1000))
    # 153
