#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 35
        The number, 197, is called a circular prime because all
        rotations of the digits: 197, 971, and 719, are themselves prime.
        There are thirteen such primes below 100:
        2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
        How many circular primes are there below one million?
"""
# =============================================================================
# (upper left label is the current label)
#
# SOLUTION: 55
#
# STATUS: [ok]
# VERIFIED: [ok]
# EXECUTION TIME: [long/ok]
# =============================================================================

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


def test_rotations(number, primes_list):
    #Sanity Check, si es 2, correcto
    if number == 2:
        #print("->", number)
        return True
    list_number = list(str(number))

    #Si en la lista hay un par, no sigo evaluando
    for i in list_number:
        if(int(i) % 2 == 0):
            return None

    #Evaluo sus rotaciones (quitando la ultima porque ya se que es primo)
    for i in range(len(list_number)-1):
        list_number.append(list_number.pop(0))
        new_prime = int("".join(list_number))
        if new_prime not in primes_list:
            return None
    #print("->", number)
    return True


def euler35(top):
    primes_list = prime_sieve(top)
    return (len([x for x in primes_list if test_rotations(x, primes_list)]))



if __name__ == "__main__":
    print(euler35(100))
    #13
    print(euler35(1000000))
    #55
