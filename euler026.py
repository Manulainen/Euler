#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 26
        A unit fraction contains 1 in the numerator.
        The decimal representation of the unit fractions with denominators
        2 to 10 are given:

        1/2	= 	0.5
        1/3	= 	0.(3)
        1/4	= 	0.25
        1/5	= 	0.2
        1/6	= 	0.1(6)
        1/7	= 	0.(142857)
        1/8	= 	0.125
        1/9	= 	0.(1)
        1/10	= 	0.1

    Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
    It can be seen that 1/7 has a 6-digit recurring cycle.
    Find the value of d < 1000 for which 1/d contains the longest
    recurring cycle in its decimal fraction part
"""
# =============================================================================
# [resuelto] 983
# [comprobado]
# =============================================================================

def div(a, b):
    q=""
    list_remainder = [a]
    while a:
        q+=str(a//b)
        a = a % b * 10
        if a == 0:
            return 0
        if a in list_remainder:
            #print("CICLE! {}/{} ->({})".format(1,b, len(q[list_remainder.index(a):])))
            return len(q[list_remainder.index(a):])
        list_remainder.append(a)

def euler26(max_d):
    max_comb = (1, 0)
    for i in range(1,max_d+1):
        len_div = div(1,i)
        if len_div > max_comb[1]:
            max_comb = (i, len_div)
    return max_comb[0]
if __name__ == "__main__":
    print(euler26(10))
    #7
    print(euler26(1000))
    #983
