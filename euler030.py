#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 30
        Surprisingly there are only three numbers that can be written as
        the sum of fourth powers of their digits:

            1634 = 1^4 + 6^4 + 3^4 + 4^4
            8208 = 8^4 + 2^4 + 0^4 + 8^4
            9474 = 9^4 + 4^4 + 7^4 + 4^4

        As 1 = 1^4 is not a sum it is not included.
        The sum of these numbers is 1634 + 8208 + 9474 = 19316.

        Find the sum of all the numbers that can be written as the
        sum of fifth powers of their digits.
"""
# =============================================================================
# (upper left label is the current label)
#
# SOLUTION: 443839
#
# STATUS: [ok]
# VERIFIED: [ok]
# EXECUTION TIME: [ok]
# =============================================================================

import matplotlib.pyplot as plt
import numpy as np

def euler30(numPower):
    totalSum = 0
    top = 300000 # Este tope deberia poder calcularse por metodo numerico
                 # Lo he sacado de la grafica a ojo... sorry
    X = np.array(range(1,top+1))
    Y = np.zeros(top)

    for i in range(2,top+1):
        cadena=list(str(i))
        sum = 0
        for num in cadena:
            sum += int(num)**numPower
        Y[i-1] = sum

        if i == sum:
            plt.scatter(i,sum, color="green", marker="X", s=200)
            totalSum += sum
            #print(i, sum)

    plt.grid(True)
    plt.plot(X,X)
    plt.scatter(X,Y, color="red", marker=".", s=1)
    return totalSum

if __name__ == "__main__":
    print(euler30(4))
    #19316
    print(euler30(5))
    #443839
