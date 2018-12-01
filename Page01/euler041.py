#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 41
        We shall say that an n-digit number is pandigital if it makes
        use of all the digits 1 to n exactly once.
        For example, 2143 is a 4-digit pandigital and is also prime.
        What is the largest n-digit pandigital prime that exists?
"""
# =============================================================================
# (upper left label is the current label)
#
# SOLUTION: 7652413
#
# STATUS: [ok]
# VERIFIED: [ok]
# EXECUTION TIME: [ok]
# =============================================================================

#bien recorro primos hasta el 987654321 y veo si son pandigitales     +
#bien recorro numeros hasta el 987654321 y veo si son primos          -
#bien recorro los pandigitales y veo si son primos                   ++
#bien recorro los pandigitales al reves y el primero que sea primo  +++

from itertools import permutations
from string import digits

#Esto genera pandigitales desde el 1 al 987654321
##Guay, pero seria mejor recorrerlo al reves 15 sec
#i=0
#for n in range(1,10):
#    perm = permutations(digits[1:],n)
#    for permutation in perm:
#        possible_prime = int("".join(permutation))
#        if is_prime(possible_prime):
#            last_prime = possible_prime
##            print(i, possible_prime, "PRIME!")
##        else:
##             print(i, possible_prime)
##        i+=1
#print(last_prime)

def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def is_n_pandigital(num):
    n = len(str(num))
    for i in range(1, n+1):
        if str(int(i)) not in str(num):
            return False
    return True

#Esto genera pandigitales desde el mayor con 9 cifras al menor con 1 cifra
def euler41():
    for n in range(9,0,-1):
        perm = permutations(digits[1:n+1][::-1], n)
        for permutation in perm:
            possible_prime = int("".join(permutation))
            if is_prime(possible_prime):
                return possible_prime

if __name__ == "__main__":
    print(euler41())
    # 7652413
