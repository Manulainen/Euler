#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 44
        Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2.
        The first ten pentagonal numbers are:
        1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

        It can be seen that P4 + P7 = 22 + 70 = 92 = P8.
        However, their difference, 70 − 22 = 48, is not pentagonal.

        Find the pair of pentagonal numbers, Pj and Pk,
        for which their sum and difference are pentagonal and
        D = |Pk − Pj| is minimised; what is the value of D?
"""
# =============================================================================
# (upper left label is the current label)
#
# SOLUTION: 5482660
#
# STATUS: [ok]
# VERIFIED: [ok]
# EXECUTION TIME: [ok]
# =============================================================================

from sympy.solvers.diophantine import diophantine
from sympy import symbols
from math import fabs, sqrt, floor, ceil

def P(n):
    return int((n * (3*n -1 ))/2)

#Inversa si la hay
def Pm1(n):
    inverse = (1+sqrt(1+24*n))/6
    if floor(inverse) == ceil(inverse):
        return True #int(inverse)
    return False

#Found 2167 1020
#None
#CPU times: user 2.21 s, sys: 1.97 ms, total: 2.21 s
#Wall time: 2.21 s
def euler44():
    i=1
    while True:
        for j in range(i, 0, -1):
            if Pm1(P(i) + P(j)) and Pm1(P(i) - P(j)):
                return int(fabs (P(i) - P(j)))
        i+=1


#def P(n):
#    return int((n*(3*n-1))/2)
#
#def generate_pentagonal_numbers():
#    n = 0
#    while True:
#        n += 1
#        yield  int((n*(3*n-1))/2)
#
## Hay que darle otra vuelta. Tarda demasiado!!
##FOUND! 2395 1020 2167
##(1020, 2167)
##CPU times: user 2min 9s, sys: 34.1 ms, total: 2min 9s
##Wall time: 2min 9s
#def euler44(): #1min 10
#    gen_pentagonal = generate_pentagonal_numbers()
#    a, b = symbols("a, b", integer=True)
#    pentagonal_list = []
#    last_pentagonal = 0
#    n=1
#    while True:
#        c = 3*n**2-n
#
#        #Pa+Pb=Pn
#        A = diophantine(3*a**2 -a +3*b**2 -b -c)
#        for j,k in A:
#            if j > 0 and k > 0 and j <= k:
#                # Estas son las respuestas positivas que resuelven Pa+Pb = Pn
##                print("P({})+P({})=P({}) ({}+{}={})".format(j,k,n, P(j), P(k), P(n)))
#
#                # Ahora compruebo si la resta genera un numero pentagonal.
#                resta = P(k)-P(j)
#                while resta >= last_pentagonal:
#                    last_pentagonal = next(gen_pentagonal)
##                    print("Generando ", last_pentagonal)
#                    pentagonal_list.append(last_pentagonal)
#
#                if resta in pentagonal_list:
##                     print("FOUND!",n, j, k)
#                     return int(fabs(resta))
#        n+=1



if __name__ == "__main__":
    print(euler44())
    # 5482660
