#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 49
        The arithmetic sequence, 1487, 4817, 8147,
        in which each of the terms increases by 3330, is unusual in two ways:
        (i) each of the three terms are prime, and,
        (ii) each of the 4-digit numbers are permutations of one another.

        There are no arithmetic sequences made up of three 1-, 2-,
        or 3-digit primes, exhibiting this property,
        but there is one other 4-digit increasing sequence.
        What 12-digit number do you form by concatenating the three terms
        in this sequence?
"""
# =============================================================================
# (upper left label is the current label)
#
# SOLUTION: 296962999629
#
# STATUS: [ok]
# VERIFIED: [ok]
# EXECUTION TIME: [ok]
# =============================================================================

import sys
sys.path.append('../../')
from Euler.EulerUtils.eulerFunctions import generate_prime, is_prime
from itertools import permutations



def d(an, a1, n=2):
    """
    devuelve el d de una progresion geometrica sabiendo el 1er elemento
    el n elemento y n.
    Por defecto considera que son consecutivos en la serie
    """
    if n == 1:
        return a1
    return int((an-a1)/(n-1))

def euler49():
    # Genero solo los primos de 4 cifras.
    gen = generate_prime(2)
    final_list = []
    while True:
        prime = next(gen)

        if len(str(prime)) == 4:
            A = permutations(str(prime),4)
            perm_dico={}
            for permutation in A:
                permutationInt = int("".join(permutation))
                if is_prime(permutationInt) and len(str(permutationInt)) == 4:
                    perm_dico[permutationInt] = 1 + perm_dico.get(permutationInt, 0)


            #if(len(perm_dico)>2):
    #            En este punto tengo listas de al menos 3 elementos, compuestas
    #            por un primo de 4 cifras y sus permutaciones  que tb son primos
    #            pero pueden estar repetidas
    #        print(prime, "   ",sorted(perm_dico))
            B = sorted(perm_dico)
            if B not in final_list:
    # =============================================================================
    # #            Aqui puedo recorrer B, que es lo que inserto en la lista final.
    #            Si el procesamiento es bueno, ni siquiera me hace falta final_list
    #            En total son 174 listas de mas o menos 10 elementos.
    # =============================================================================

                final_list.append(B)
                for i in range(len(B)):
                    for num in B[1+i:]:
                        D = (d(num, B[i]))
                        if B[i] +D in B and B[i] +2*D in B:
                            print("{}{}{}".format(B[i], B[i]+ D, B[i]+ 2*D))

        if len(str(prime)) > 4:
            break

if __name__ == "__main__":
    print(euler49())
    # 296962999629