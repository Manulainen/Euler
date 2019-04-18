#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 070
        Euler's Totient function, φ(n) [sometimes called the phi function],
        is used to determine the number of positive numbers less than or equal
        to n which are relatively prime to n.
        For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and
        relatively prime to nine, φ(9)=6.

        The number 1 is considered to be relatively prime
        to every positive number, so φ(1)=1.

        Interestingly, φ(87109)=79180, and it can be seen
        that 87109 is a permutation of 79180.

        Find the value of n, 1 < n < 10^7, for which φ(n) is a
        permutation of n and the ratio n/φ(n) produces a minimum.
"""
# =============================================================================
# (upper left label is the current label)
#
# SOLUTION: 8319823
#
# STATUS: [ok]
# VERIFIED: [ok]
# EXECUTION TIME: [ok]
# =============================================================================

# Remove if not necessary
import sys
sys.path.append('../')
# sys.path.append('../../')

from Euler.EulerUtils import eulerFunctions as ef


def euler070(top):
    pgen = ef.generate_prime(2)
    prime = next(pgen)


    """
    Genero primos en principio hasta 10^7 / 2. Pero se que la solucion optima esta
    cerca de primos que sean sqrt(10^7) porque la multiplicacion es maxima si ambos valores
    valen lo mismo (pero no pueden porque no hay numero n y n-1 que sean permutacion)
    Así que calculo primos hasta un poco mas que sqrt(10^7)
    """
    P=[]
    while prime <= 3600:
        P.append(prime)
        prime = next(pgen)



    """
    Dada una lista  P= [2,3,5,7,11,13,17,19,23,29] (primos hasta la mitad de tope)
    calcula las multiplicaciones 2 a 2 de elementos que no superen un tope

    res es una tupla con n buscado y ratio minimo que se va actualizando por cada n y phi(n) permutados
    φ(m.n) si m y n son primos es (m-1) . (n-1)
    """
    res = 0,2
    for i, prime in enumerate(P):
        for j in range(i+1, len(P)):
            n = prime * P[j]
            if n > top:
                break # este break me evita todas las combinaciones.
            else:
                phi = (prime-1) * (P[j] - 1)
                if ef.is_permutation(n, phi):
                    #print('N:{} ({}.{})   φ({})={} Ratio:{}'.format(n, prime, P[j], n, phi, n/phi))
                    if n/phi < res[1]:
                        res = n, n/phi
    return res



if __name__ == "__main__":
    print(euler070(10000000))
    #(8319823, 1.0007090511248113)
