#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 5
        2520 is the smallest number that can be divided by each of the numbers
        from 1 to 10 without any remainder.
        What is the smallest positive number that is evenly divisible by all
        of the numbers from 1 to 20?
"""
# =============================================================================
# [resuelto] 232792560
# [comprobado]
# =============================================================================

# es mas de 66 millones...
#   devuelve el primer numero que sea divisible por max_divisor y todos los
#    numeros bajo el. si max_divisor es 3, busca el 1` numero divisible
#    por 2 y por 3 a la vez

# print(euler5(10))
# 2520
# print(euler5(20))
# 232792560

def euler5(max_divisor):
    divisor = 2
    cont = 1
    gap = 1
    while(divisor <= max_divisor):
        if cont%divisor == 0:
            divisor += 1
            gap = cont
            continue
        cont += gap
    return cont



if __name__ == "__main__":
    print(euler5(10))
    # 2520
    print(euler5(20))
    # 232792560

