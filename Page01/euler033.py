#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 33
        The fraction 49/98 is a curious fraction, as an inexperienced
        mathematician in attempting to simplify it may incorrectly believe
        that 49/98 = 4/8, which is correct,
        is obtained by cancelling the 9s.

        We shall consider fractions like, 30/50 = 3/5,
        to be trivial examples.

        There are exactly four non-trivial examples of this
        type of fraction, less than one in value, and containing two
        digits in the numerator and denominator.

        If the product of these four fractions is given in its
        lowest common terms, find the value of the denominator.
"""
# =============================================================================
# (upper left label is the current label)
#
# SOLUTION: 100
#
# STATUS: [ok]
# VERIFIED: [ok]
# EXECUTION TIME: [ok]
# =============================================================================

import fractions

def euler33():
    fraction_list=[]
    #Verifico fracciones desde 11/12 a 98/99
    for num in range(11,100):
        #Quito las triviales
        if num % 10 != 0:
            for den in range(num + 1, 100):
                #Quito las triviales
                if den % 10 != 0:
                    numT = tuple([int(i) for i in str(num)])
                    denT = tuple([int(i) for i in str(den)])

                    #Si tienen interseccion de 1 digito compruebo si quitandosela
                    #evaluan a lo mismo
                    inters = tuple(set(numT).intersection(denT))
                    if len(inters) == 1:
                        numT = tuple(set(numT).difference(inters))
                        denT = tuple(set(denT).difference(inters))

                        #Al hacer la diferencia 11 -1 queda (), en esos casos en
                        # que se queda vacia la tupla, inserto la interseccion
                        if not numT:
                            numT = inters
                        if not denT:
                            denT = inters

                        numT = int(numT[0])
                        denT = int(denT[0])
                        if num/den ==  numT/denT:
                            #print("[",num, '/', den,"]", inters, "[",numT, '/', denT,"]")
                            fraction_list.append(fractions.Fraction(num, den))

    #Multiplico las fracciones, reduzco y obtengo el denominador
    prod_fraction=fractions.Fraction(1, 1)
    for i in fraction_list:
        prod_fraction*=i
    return prod_fraction.denominator

#[ 16 / 64 ] (6) [ 1 / 4 ]
#[ 19 / 95 ] (9) [ 1 / 5 ]
#[ 26 / 65 ] (6) [ 2 / 5 ]
#[ 49 / 98 ] (9) [ 4 / 8 ]

if __name__ == "__main__":
    print(euler33())
    #100
