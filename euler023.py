#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 23
        A perfect number is a number for which the sum of its proper
        divisors is exactly equal to the number.
        For example, the sum of the proper divisors of 28 would be
        1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

        A number n is called deficient if the sum of its proper divisors
        is less than n and it is called abundant if this sum exceeds n.

        As 12 is the smallest abundant number,
        1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written
        as the sum of two abundant numbers is 24. By mathematical analysis,
        it can be shown that all integers greater than 28123 can be written
        as the sum of two abundant numbers. However, this upper limit cannot
        be reduced any further by analysis even though it is known that the
        greatest number that cannot be expressed as the sum of two abundant
        numbers is less than this limit.

        Find the sum of all the positive integers which cannot
        be written as the sum of two abundant numbers.

"""

# =============================================================================
# [resuelto] 4179871
# [comprobado]
# =============================================================================

from itertools import combinations_with_replacement
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



def euler23():
    """
    Fuerza bruta, de cada numero hasta 28123 veamos si es abundante, deficiente o
    perfecto.
    Salen 6965 abundantes, 4 perfectos, y 21154 deficientes (mongers)
    Puedo hacer un vector de 1 a 28123 de trues
    Si hago todas las sumas posibles de 2 abundantes (menors que 28123) y voy
    tachando los elementos del vector, al final tendré sólo numeros que
    no pueden ser suma de 2 abundantes.
    """

    #De aqui saco solo la lista de abundantes
    #
    abundant_list=[]
    for i in range(1, 28123+1):
        sum_list_divisors = sum(get_all_divisors(get_prime_factors(i)))
        if sum_list_divisors > i:
            abundant_list.append(i)

    # Hago todas las combinaciones de 2 elementos de esa lista cuya suma sea
    # menor que 28123 (28124 porque empieza en 0!)
    #
    no_sum_abundant_number_list=[False]*28124
    for a1, a2 in (combinations_with_replacement(abundant_list, 2)):
        if a1 + a2 <= 28123:
            no_sum_abundant_number_list[a1+a2] = True

    #print("LIST TO SUM: ", len(no_sum_abundant_number_list))

    # Sumo todos los elementos que no hayan sido tachados antes.
    return sum([index for index, num in enumerate(no_sum_abundant_number_list)
                     if num == False])

if __name__ == "__main__":
    print(euler23())
    #4179871