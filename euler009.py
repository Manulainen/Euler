#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    EULER 9
        A Pythagorean triplet is a set of three natural numbers,
        a < b < c, for which, a² + b² = c²
        For example, 3² + 4² = 9 + 16 = 25 = 5².
        There exists exactly one Pythagorean triplet for which a + b + c = 1000
        Find the product abc.
"""

# =============================================================================
# [resuelto] 31875000
# [comprobado]
#
# print(euler9(12))
# 3 4 5 60
# print(euler9(1000))
# (375, 200, 425, 31875000)

# =============================================================================

def triplet(m, n):
    if m >= n:
        print(" m < n ")
    else:
        a = n**2 - m**2
        b = 2*n*m
        c = n**2 + m**2
        return a, b, c

def generate_triplet():
    m = 1
    n = 2
    while True:
        if m == n:
            m = 1
            n += 1
        yield triplet(m, n)
        m += 1

def euler9(total_sum):
    suma = 0
    it = generate_triplet()
    while suma != total_sum:
        a,b,c = next(it)
        suma = a+b+c
    return(a,b,c, a*b*c)


if __name__ == "__main__":
    print(euler9(12))
    #(3 4 5 60)
    print(euler9(1000))
    #(375, 200, 425, 31875000)

