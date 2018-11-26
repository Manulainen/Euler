#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt

"""
    EULER 10
        The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
        Find the sum of all the primes below two million.
"""
# =============================================================================
# (upper left label is the current label)
#
# SOLUTION: 142913828922
#
# STATUS: [ok]
# VERIFIED: [ok]
# EXECUTION TIME: [ok]
# =============================================================================

# Old generate_prime function. Unefficient!
#def generate_prime():
#    j=2
#    while True:
#        i =2
#        k=sqrt(j)
#        while i<=k:
#            if j%i==0:
#                break
#            i=i+1
#        if i>k:
#            yield j
#        j +=1
#
#def euler10(max_prime):
#    it = generate_prime()
#    prime = 0
#    total_sum = 0
#    while True:
#        prime = next(it)
#        if prime > max_prime:
#            break
#        # Prime that fills condition
#        total_sum += prime
#        #print(prime)
#    return total_sum


# Este esta mas optimizado
#Tarda menos de un segundo.
# Crea una lista con los numeros hasta limit.
#recorre la lista tachando los que son multiplos del i y al final queda una
# lista con los primos hasta el limit.
def prime_sieve(limit):
    a = [True] * limit
    a[0] = a[1] = False
    primes = []
    for i, isprime in enumerate(a):
        if isprime:
            primes.append(i)
            for n in range(0, limit, i):
                a[n] = False
    return primes


def euler10(limit):
    primes = prime_sieve(limit)
    return(sum(primes))


if __name__ == "__main__":
    print(euler10(10))
# 17
    print(euler10(2000000))
# 142913828922









