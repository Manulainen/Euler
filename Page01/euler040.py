#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 40
        An irrational decimal fraction is created by
        concatenating the positive integers:

        0.123456789101112131415161718192021...
                     ^
        It can be seen that the 12th digit of the fractional part is 1.
        If dn represents the nth digit of the fractional part,
        find the value of the following expression.

        d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""
# =============================================================================
# (upper left label is the current label)
#
# SOLUTION: 210
#
# STATUS: [ok]
# VERIFIED: [ok]
# EXECUTION TIME: [ok]
# =============================================================================

from math import floor

# Forma fea fuerza bruta (muy poco eficiente con numeros altos).
#
def RUMAeuler40():
    a=""
    i=0
    while len(a) < 1000001:
        a += str(i)
        i+=1
    print(a[1], a[10], a[100], a[1000], a[10000], a[100000], a[1000000], "->",
          int(a[1])*
          int(a[10])*
          int(a[100])*
          int(a[1000])*
          int(a[10000])*
          int(a[100000])*
          int(a[1000000]))
#1 1 5 3 7 2 1 -> 210

# Forma guay calculando posiciones relativas. (muy eficiente)
def get_num_ciphers(index):
    """
    el bloque de 1 cifra tiene 9 pos de 1 digito [1-9]         9.10^0 * 1 char
    el bloque de 2 cifras tiene 180 pos de 1 digito [10-99]    9.10^1 * 2 char
    el bloque de 3 cifras tiene 2700 pos de 1 digito [100-999] 9.10^2 * 3 char

    esta funcion devuelve el bloque al que pertenece el index
    (1, 2, 3 o 4 cifras) y su posicion relativa (empezando en 0).

    get_num_ciphers(1)    la pos 0 del bloque de 1 cifras
    get_num_ciphers(9)    la pos 8 del bloque de 1 cifras
    get_num_ciphers(10)   la pos 0 del bloque de 2 cifras
    get_num_ciphers(12)   la pos 2 del bloque de 2 cifras
    get_num_ciphers(189)  la pos 179 del bloque de 2 cifras
    get_num_ciphers(190)  la pos 0 del bloque de 3 cifras
    get_num_ciphers(2889) la pos 2699 del bloque de 3 cifras
    get_num_ciphers(2890) la pos 0 del bloque de 4 cifras
    """

    last_index_in_block=0
    last_index_in_prev_block=0
    num_ciphers = 1
    while(True):
        last_index_in_block += 9 * 10**(num_ciphers - 1) * num_ciphers
        if(index - last_index_in_block) <= 0:
#            print("la pos {} del bloque de {} cifras ".format(
#                    index - last_index_in_prev_block - 1, num_ciphers))
            return index - last_index_in_prev_block - 1, num_ciphers
        num_ciphers += 1
        last_index_in_prev_block = last_index_in_block

def get_exact_digit(d):
    """
    block 1 empieza en 1
    block 2 empieza en 10
    block 3 empieza en 100
    """

    index, block = get_num_ciphers(d)

    real_number = 10**(block-1) + floor(index/block)
#    print(real_number, index%block)
    return int(str(real_number)[index%block])



def euler40():
    return get_exact_digit(1) * get_exact_digit(10) * get_exact_digit(100) *\
        get_exact_digit(1000) * get_exact_digit(10000) *\
        get_exact_digit(100000)  * get_exact_digit(1000000)


if __name__ == "__main__":
    print(euler40())
    #210
