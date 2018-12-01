#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 32
        We shall say that an n-digit number is pandigital if it
        makes use of all the digits 1 to n exactly once;
        for example, the 5-digit number, 15234, is 1 through 5 pandigital.

        The product 7254 is unusual, as the identity, 39 × 186 = 7254,
        containing multiplicand, multiplier, and product
        is 1 through 9 pandigital.

        Find the sum of all products whose multiplicand/multiplier/product
        identity can be written as a 1 through 9 pandigital.
        HINT: Some products can be obtained in more than one way so
        be sure to only include it once in your sum.

"""
# =============================================================================
# (upper left label is the current label)
#
# SOLUTION: 45228
#
# STATUS: [ok]
# VERIFIED: [ok]
# EXECUTION TIME: [ok]
# =============================================================================

import itertools

def euler32():
    entire_tuple = (1,2,3,4,5,6,7,8,9)
    d = dict()

    #4c * 1c = 4c
    tupla_it=itertools.permutations(range(1,10), 4)
    for i, tpl in enumerate(tupla_it):
        difference = tuple(set(entire_tuple).symmetric_difference(set(tpl)))
        tupla_it2=itertools.permutations(difference, 1)
        for j, tpl2 in enumerate(tupla_it2):
            #print(tpl, tpl2)
            mult1 = int(str(tpl[0]) + str(tpl[1]) + str(tpl[2]) + str(tpl[3]))
            mult2 = int(str(tpl2[0]))

            union = tuple(set(tpl).union(set(tpl2)))
            differenceP= tuple(set(entire_tuple).symmetric_difference(union))


            product = mult1*mult2
            pTuple = tuple([int(i) for i in str(product)])
            if(len(str(product)) == 4):
                if not tuple(set(pTuple).symmetric_difference(differenceP)):
                    #print(mult1, mult2, product, pTuple, differenceP)
                    d[product] = 1+ d.get(product, 0)

    #3c * 2c = 4c
    tupla_it=itertools.permutations(range(1,10), 3)
    for i, tpl in enumerate(tupla_it):
        difference = tuple(set(entire_tuple).symmetric_difference(set(tpl)))
        tupla_it2=itertools.permutations(difference, 2)
        for j, tpl2 in enumerate(tupla_it2):
            #print(tpl, tpl2)
            mult1 = int(str(tpl[0]) + str(tpl[1]) + str(tpl[2]))
            mult2 = int(str(tpl2[0])+ str(tpl2[1]))

            union = tuple(set(tpl).union(set(tpl2)))
            differenceP= tuple(set(entire_tuple).symmetric_difference(union))

            product = mult1*mult2
            pTuple = tuple([int(i) for i in str(product)])
            if(len(str(product)) == 4):
                    if not tuple(set(pTuple).symmetric_difference(differenceP)):
                        #print(mult1, mult2, product,pTuple, differenceP)
                        d[product] = 1+ d.get(product, 0)

    total = 0
    for i in d.keys():
        total += i
    return total

if __name__ == "__main__":
    print(euler32())
    # 45228
