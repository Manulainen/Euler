#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 43
        The number, 1406357289, is a 0 to 9 pandigital number
        because it is made up of each of the digits 0 to 9 in some order,
        but it also has a rather interesting sub-string divisibility property.
        Let d1 be the 1st digit, d2 be the 2nd digit, and so on.
        In this way, we note the following:

        d2d3d4=406 is divisible by 2
        d3d4d5=063 is divisible by 3
        d4d5d6=635 is divisible by 5
        d5d6d7=357 is divisible by 7
        d6d7d8=572 is divisible by 11
        d7d8d9=728 is divisible by 13
        d8d9d10=289 is divisible by 17

        Find the sum of all 0 to 9 pandigital numbers with this property.
"""
# =============================================================================
# (upper left label is the current label)
#
# SOLUTION: 16695334890
#
# STATUS: [ok]
# VERIFIED: [ok]
# EXECUTION TIME: [ok]
# =============================================================================

from string import digits
from itertools import permutations


#        d2d3d4=406 is divisible by 2    div2
#        d3d4d5=063 is divisible by 3    div3
#        d4d5d6=635 is divisible by 5    div5
#        d5d6d7=357 is divisible by 7    div7
#        d6d7d8=572 is divisible by 11   div11
#        d7d8d9=728 is divisible by 13   div13
#        d8d9d10=289 is divisible by 17  div17

def euler43():
#    Se puede analizar los numeros para sacar reglas, pero por fuerza bruta
#    tarda menos de 5 segundos, asi que esta bastante bien.
#    En el bucle recorro unicamente los pandigitales, asi que hay muchas
#    menos iteraciones
    total_sum=0
    perm = permutations(digits, len(digits))
    for i in perm:
        strnumber = "".join(i)
        div2 = int(strnumber[1:4])
        if div2 % 2 != 0:
            continue

        div3 = int(strnumber[2:5])
        if div3 % 3 != 0:
            continue

        div5 = int(strnumber[3:6])
        if div5 % 5 != 0:
            continue

        div7 = int(strnumber[4:7])
        if div7 % 7 != 0:
            continue

        div11 = int(strnumber[5:8])
        if div11 % 11 != 0:
            continue

        div13 = int(strnumber[6:9])
        if div13 % 13 != 0:
            continue

        div17 = int(strnumber[7:10])
        if div17 % 17 != 0:
            continue

        total_sum += int(strnumber)
    return total_sum


if __name__ == "__main__":
    print(euler43())
    # 16695334890
