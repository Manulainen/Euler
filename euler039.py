#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 39
        If p is the perimeter of a right angle triangle with integral
        length sides, {a,b,c}, there are exactly
        three solutions for p = 120.
        {20,48,52}, {24,45,51}, {30,40,50}

        For which value of p ≤ 1000,
        is the number of solutions maximised?
"""
# =============================================================================
# (upper left label is the current label)
#
# SOLUTION: 840
#
# STATUS: [ok]
# VERIFIED: [ok]
# EXECUTION TIME: [long/ok]
# =============================================================================

from sympy.solvers.diophantine import diophantine
from sympy import symbols

def euler39():
    #No puede haber un P impar, en la ecuacion hay que resolver un P²/2
    #
    maxSolutions = 0
    for P in range(2,1001,2):
        a,b,c = symbols("a,b,c", integer=True)
        ecu = diophantine(P*a +P*b -a*b - P**2/2)

        A= list(ecu)
        posList=[]
        for a,b in A:
            # a y b positivos
            if a>0 and b>0:
                # a,b es lo mismo que b,a solo inserto una vez.
                if (b,a) not in posList:
                    if P - a - b >0:
                        posList.append((a,b))
        if len(posList) >= maxSolutions:
            maxSolutions = len(posList)
            maxP = P

        #print(P, posList, len(posList))
    return maxP

if __name__ == "__main__":
    print(euler39())
    # 840
