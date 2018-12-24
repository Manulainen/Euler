#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 051
        By replacing the 1st digit of the 2-digit number *3,
        it turns out that six of the nine possible values:
        13, 23, 43, 53, 73, and 83, are all prime.

        By replacing the 3rd and 4th digits of 56**3 with the same digit,
        this 5-digit number is the first example having seven primes
        among the ten generated numbers, yielding the family:
        56003, 56113, 56333, 56443, 56663, 56773, and 56993.

        Consequently 56003, being the first member of this family,
        is the smallest prime with this property.

        Find the smallest prime which, by replacing part of the number
        (not necessarily adjacent digits) with the same digit,
        is part of an eight prime value family.
"""
# =============================================================================
# (upper left label is the current label)
#
# SOLUTION: 121313
#
# STATUS: [ok]
# VERIFIED: [ok]
# EXECUTION TIME: [ok]
# =============================================================================

import sys
sys.path.append('../../')
sys.path.append('../')
from Euler.EulerUtils import eulerFunctions as ef

# permutation_without_n (9*1)
# mira las 10 opciones para *. Corta antes si encuentra demasiados no primos
# o si encuentra el numero correcto de primos
#
def tests_iterations(permutation_to_loop, number_of_primes_in_family ):
#    print("tests_iterations ", permutation_to_loop)
    if "*" in permutation_to_loop:
        totalprimos = 0
        total_no_primos = 0
        found = None
        for i in range(10):
            #MIRAR SI ES PRIMO
            num = int(permutation_to_loop.replace("*",str(i)))

            ###### SANITY CHECK: un * a la izquierda no puede ser 0
            #
            if len(str(num)) == len(permutation_to_loop):
                if ef.is_prime(num):
                    totalprimos += 1
                else:
                    total_no_primos += 1
#                print("*****", num, ef.is_prime(num))

                ###### SANITY CHECK: Si hay mas de 4 no_primos,
                #                    el maximo de primos de la iteracion es de 6
                #
                if total_no_primos > 10 - number_of_primes_in_family:
#                    print("Iteracion {} palma con {} primos".format(permutation_to_loop, totalprimos))
                    break

                if totalprimos == number_of_primes_in_family:
#                    print("  FOUND!!!! iteracion [{}] con {} primos".format(permutation_to_loop, totalprimos))
                    found = permutation_to_loop
                    break

    return found

def euler051(number_of_primes_in_family):

    ## Desde el primer primo de 2 cifras distintas
    prime_generator =  ef.generate_prime(13)
    found = False
    while found != True:
        prime = next(prime_generator)
    #    print("#########################")
    #    print("[{}]".format(prime))
        s = set()
        for cipher in str(prime):
            permutation_to_loop = str(prime).replace(cipher,"*")

            ###### SANITY CHECK: un * al final como mucho genera 4 primos
            #
            if permutation_to_loop[len(permutation_to_loop) - 1] != "*":
                if permutation_to_loop not in s:
                    s.add(permutation_to_loop)

    #                print(permutation_to_loop)
                    if tests_iterations(permutation_to_loop, number_of_primes_in_family) != None:
                        found = True
                        break
    return prime

if __name__ == "__main__":
    print(euler051(6))
    # 13
    print(euler051(7))
    # 56003
    print(euler051(8))
    # 121313
