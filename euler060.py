#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 060
        The primes 3, 7, 109, and 673, are quite remarkable.
        By taking any two primes and concatenating them in any order the
        result will always be prime. For example, taking 7 and 109,
        both 7109 and 1097 are prime. The sum of these four primes, 792,
        represents the lowest sum for a set of four primes with this property.
        Find the lowest sum for a set of five primes for which
        any two primes concatenate to produce another prime.
"""
# =============================================================================
# (upper left label is the current label)
#
# SOLUTION: 26033
#
# STATUS: [ok]
# VERIFIED: [ok]
# EXECUTION TIME: [unacceptable/long/ok]
# =============================================================================

import sys
sys.path.append('../')
sys.path.append('../../')
from Euler.EulerUtils import eulerFunctions as ef
from itertools import combinations



def is_concat_prime(m, n):
    possible_primeL = int(str(m) + str(n))
    possible_primeR = int(str(n) + str(m))
    if ef.is_prime(possible_primeL) and ef.is_prime(possible_primeR):
        return True
    return False


prime_generator = ef.generate_prime(2)
prime_list = []
g2 = []
g3 = []
g4 = []
g5 = []

def euler060():
    found  = False

    while found != True:

        # 1 GENERO UN PRIMO
        prime = next(prime_generator)


        # 2 Recorro todos los primos menores que el. si son concatenables creo tupla de 2 a g2
        # Se crea una lista temporal con los primos
        lista_temporal = []
        for j in prime_list:
            if is_concat_prime(j, prime):
                pareja =  tuple(sorted((prime, j)))
                g2.append(pareja)

                lista_temporal.append(j)

        # si hay en  la lista temporal una combinacion de 2 que exista en g2, ya tengo una tupla de 3
        perm = combinations(lista_temporal, 2)
        for p1, p2 in perm:
            T = (tuple(sorted((p1, p2))))
            if T in g2:
                g3.append(tuple(sorted((prime,p1,p2))))

        # si hay en  la lista temporal una combinacion de 3 que exista en g3, ya tengo una tupla de 4
        perm = combinations(lista_temporal, 3)
        for p1, p2, p3 in perm:
            T = (tuple(sorted((p1, p2, p3))))
            if T in g3:
                g4.append(tuple(sorted((prime,p1,p2, p3))))

        # si hay en  la lista temporal una combinacion de 4 que exista en g4, ya tengo una tupla de 5
        perm = combinations(lista_temporal, 4)
        for p1, p2, p3, p4 in perm:
            T = (tuple(sorted((p1, p2, p3, p4))))
            if T in g4:
                g5.append(tuple(sorted((prime,p1,p2, p3, p4))))
                solution =  tuple(sorted((prime, p1, p2, p3, p4)))
                found = True

        prime_list.append(prime)

    return solution, sum(solution)

if __name__ == "__main__":
    print(euler060())
    # SOLUTION 26033
