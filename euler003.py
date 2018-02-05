#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 3
        The prime factors of 13195 are 5, 7, 13 and 29.
        What is the largest prime factor of the number 600851475143?
"""
# =============================================================================
# [resuelto] 6857
# [comprobado]
#
# print(euler3(13195))
# [5, 7, 13, 29]
# print(euler3(600851475143))
# [71, 839, 1471, 6857]
# =============================================================================

def euler3(big_number):
    """
    Voy iterando numeros hasta que el big_number sea divisible.
    Cuando encuentro un divisible, lo inserto en la lista. El resultado de la
    division es el nuevo tope del contador.
    Repito el proceso iniciando el contador en el último divisible encontrado.
    El proceso se repite hasta que el contador llegue al tope.
    La lista no va a ser muy muy larga, asi que no hace falta usar generadores.

    Parameters
    ----------
    big_number : int
        Number to be factorized into primes

    -----

    Returns
    -------
    prime_divisor_list: list
        List containing the factorized primes increasing order
    """
    prime_divisor_list = []
    tope = big_number
    cont = 2
    while cont <= tope:
        if tope%cont == 0:
            prime_divisor_list.append(cont)
            if tope/cont == 1:
                break
            else:
                tope = tope/cont
                continue
        cont += 1
    return prime_divisor_list


if __name__ == "__main__":
    print(euler3(13195))
#[5, 7, 13, 29]
    print(euler3(600851475143))
#[71, 839, 1471, 6857]
