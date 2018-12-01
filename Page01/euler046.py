#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 46
        It was proposed by Christian Goldbach that every odd composite
        number can be written as the sum of a prime and twice a square.
        9 = 7 + 2×1^2
        15 = 7 + 2×2^2
        21 = 3 + 2×3^2
        25 = 7 + 2×3^2
        27 = 19 + 2×2^2
        33 = 31 + 2×1^2
        It turns out that the conjecture was false.

        What is the smallest odd composite that cannot be
        written as the sum of a prime and twice a square?
"""
# =============================================================================
# (upper left label is the current label)
#
# SOLUTION: 5777
#
# STATUS: [ok]
# VERIFIED: [ok]
# EXECUTION TIME: [ok]
# =============================================================================

from math import sqrt

def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def generate_prime():
    j=2
    while True:
        i =2
        k=sqrt(j)
        while i<=k:
            if j%i==0:
                break
            i=i+1
        if i>k:
            yield j
        j +=1

def euler46():
    i=3 #1 es odd pero no es composite
    while True:
       if not is_prime(i):
           #Genera impares no primos (odd composite)
          # print("CANDIDATO", i)
           pGen = generate_prime()
           prime = 2
           while prime < i:
               resta = i - prime
               # resta = 2.x^2, asi que x = (sqrt(2.resta))/2
               x= (sqrt(2*resta))/2
               if x == int(x): #igual que el floor(x) == ceil(x) del anterior
                  # print("{} = {} + 2*{}^2".format(i, prime, int(x)))
                  #Se puede escribir bajo la formula de Goldbach, asi que fuera
                   break
               prime = next(pGen)
            #Llegado a este punto, no se puede encontrar una expresion y found
           if prime > i:
               return i
       i+=2

if __name__ == "__main__":
    print(euler46())
    # 5777
