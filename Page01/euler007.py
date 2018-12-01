#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt

"""
    EULER 7
        By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
        we can see that the 6th prime is 13.
        What is the 10001st prime number?
"""
# =============================================================================
# (upper left label is the current label)
#
# SOLUTION: 104743
#
# STATUS: [ok]
# VERIFIED: [ok]
# EXECUTION TIME: [ok]
# =============================================================================

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

def euler7(top):
    it = generate_prime()
    last_prime = 0
    for i in range(top):
        last_prime = next(it)
    return last_prime

if __name__ == "__main__":
    print(euler7(6))
# 13
    print(euler7(10001))
# 104743
