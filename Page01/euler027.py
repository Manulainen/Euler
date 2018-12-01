#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 27
        Euler discovered the remarkable quadratic formula:
        n^2+n+41

        It turns out that the formula will produce 40 primes for the
        consecutive integer values 0≤n≤39
        However, when n=40,402+40+41=40(40+1)+41 is divisible by 41,
        and certainly when n=41,412+41+41 is clearly divisible by 41.

        The incredible formula n^2−79n+1601 was discovered, which produces
        80 primes for the consecutive values 0≤n≤79.

        The product of the coefficients, −79 and 1601, is −126479.
        Considering quadratics of the form:
        n^2+an+b, where |a|<1000 and |b|≤1000
        where |n| is the modulus/absolute value of n e.g. |11|=11 and |−4|=4

        Find the product of the coefficients, a and b,
        for the quadratic expression that produces the maximum number
        of primes for consecutive values of n, starting with n=0.

"""
# =============================================================================
# (upper left label is the current label)
#
# SOLUTION:  -59231
#
# STATUS: [ok]
# VERIFIED: [ok]
# EXECUTION TIME: [ok]
# =============================================================================

def is_prime6k(n):
    if n <= 1:
       return False
    elif n <= 3:
       return True
    elif n % 2 == 0 or n % 3 == 0:
       return False
    i= 5
    while i * i <= n:
       if n % i == 0 or n % (i + 2) == 0:
           return False
       i += + 6
    return True

def euler27():
    final = (0,0,0)
    for a in range(-999,999+1):
        for b in range(-1000,1000+1):
            n=0
            while True:
                y =  n**2+a*n+b
                if not is_prime6k(y):
                    break
                n+=1

            if n > final[2]:
                final = (a, b , n)
    return final[0]*final[1]


if __name__ == "__main__":
    print(euler27())
    # -59231
