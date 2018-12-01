#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 34
        145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
        Find the sum of all numbers which are equal to
        the sum of the factorial of their digits.
        Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
# =============================================================================
# (upper left label is the current label)
#
# SOLUTION: 40730
#
# STATUS: [ok]
# VERIFIED: [ok]
# EXECUTION TIME: [long/ok]
# =============================================================================

import matplotlib.pyplot as plt
from math import factorial as fact
import numpy as np


def euler34():

    # Cerca del 2000000 el minimo factorial ya es mayor que el
    # X, no hace falta seguir  Verificando
    #
    top = 2000000
    X = np.array(range(top))
    Y = np.array(range(top))

    sumTotal = 0
    for i in range(3, top):
        A = sum((fact(int(x)) for x in list(str(i))))
        Y[i] = A
        if i == A:
            #print(i, A)
            sumTotal +=i

    plt.scatter(X,Y, s=1)
    plt.plot(X,X)
    return sumTotal


if __name__ == "__main__":
   print(euler34())
    # 40730
