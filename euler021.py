#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 21
        Let d(n) be defined as the sum of proper divisors of n
        (numbers less than n which divide evenly into n).
        If d(a) = b and d(b) = a, where a ≠ b, then a and b are an
        amicable pair and each of a and b are called amicable numbers.

        For example, the proper divisors of 220 are
        1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
        The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

        Evaluate the sum of all the amicable numbers under 10000.

"""

# =============================================================================
# [resuelto] 31626
# [comprobar]
# =============================================================================

from itertools import product

def get_all_divisors(dico):
    """
    Dado un diccionaro de factores primos, genera todos los factores posibles,
    que no es mas que todas las posibles combinaciones de factores primos entre
    si
    """
    base = [x for x in dico.keys()]
    potencias = [range(x+1) for x in dico.values()]
    list_factors = []
    for i in product(*potencias):
        """
        [a**b for a,b in zip(base,i)]
        Genera por cada i distinto una lista de factores que entre si hay
        que multiplicar
        """
        factor_list = ([a**b for a,b in zip(base,i)])
        total = 1
        for a in factor_list:
            total *= a
        list_factors.append(total)
    del list_factors[-1] # Esto es para no sumar el ultimo
    return list_factors

def get_prime_factors(big_number):
    """
    Genera un diccionario con los factores primos en clave y frecuencias en
    valor.
    28 -> 2*2*7 -> 2:2, 7:1
    220 -> 2*2*5*11 -> 2:2, 5:1, 11:1
    """
    divisor = 2
    prime_divisor_dic = {}
    while big_number != 1:
        if big_number % divisor == 0:
            big_number = big_number / divisor
            prime_divisor_dic[divisor] = 1 + prime_divisor_dic.get(divisor, 0)
        else:
            divisor +=1
    return prime_divisor_dic

def d(big_number):
    """
    devuelve la suma de todos los factores propios de n
    (numeros menores que n que son divisores de n)
    d(220) -> [1, 11, 5, 55, 2, 22, 10, 110, 4, 44, 20] -> 284
    d(284) -> [1, 71, 2, 142, 4] -> 220
    """
    list_divisors = get_all_divisors(get_prime_factors(big_number))
    #print(list_divisors)
    return sum(list_divisors)


def euler21(max):
    final_list=[]
    visited=[]
    for i in range(2, max+1):
        if(i != d(i) and i == d(d(i)) and i not in visited):
            visited.append(d(i))
            final_list.append(i)
            final_list.append(d(i))
    print(final_list)
    return sum(final_list)


if __name__ == "__main__":
    print(euler21(10000))
    #31626
