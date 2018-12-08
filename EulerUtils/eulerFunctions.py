#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date: 18/05/2018
Version: 0.1
"""

from math import sqrt, floor, ceil
import string
from sympy.solvers.diophantine import diophantine
from sympy import symbols

# =============================================================================
# HINT PRIMOS
# =============================================================================

def is_prime(n):
    """
    Devuelve True si n es primo.
    """

    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def generate_prime(n):
    """
    Generador que empezando en n, va soltando primos
    """

    j=n
    while True:
        i =2
        k=sqrt(j)
        while i<=k:
            if j%i==0:
                break
            i=i+1
        if i>k:
            yield j
        j +=1

def prime_sieve(limit):
    """
    Devuelve una lista con los primos hasta el limite pasado por argumento
    """

    a = [True] * limit
    a[0] = a[1] = False
    primes = []
    for i, isprime in enumerate(a):
        if isprime:
            primes.append(i)
            for n in range(0, limit, i):
                a[n] = False
    return primes

# =============================================================================
# HINT TRIANGULAR, PENTAGONAL, HEXAGONAL
# =============================================================================

def T(n):
    return int((n * (n +1))/2)

def P(n):
    return int((n * (3*n -1))/2)

def H(n):
    return int(n * (2*n -1))

def isT(n):
    inverse = (-1+sqrt(1+8*n))/2
    if floor(inverse) == ceil(inverse):
        return True #int(inverse)
    return False

def isP(n):
    inverse = (1+sqrt(1+24*n))/6
    if floor(inverse) == ceil(inverse):
        return True #int(inverse)
    return False

def isH(n):
    inverse = (1+sqrt(1+8*n))/4
    if floor(inverse) == ceil(inverse):
        return True #int(inverse)
    return False


# =============================================================================
# HINT NAME SCORE
# =============================================================================

UPPER_ASCII = string.ascii_uppercase

def get_char_pos(list_ascii, char):
    return list_ascii.index(char) + 1

def get_name_score(UPPER_ASCII, name):
    """
    Dado una lista de ascii y un nombre devuelve su puntiacion,
    que es la suma de sus caracteres pasados a ascii
    """
    score = 0
    for letter in name:
        score += get_char_pos(list_ascii, letter)
    return score


# =============================================================================
# HINT DIOPHANTINES
# =============================================================================

a,b,c,d,e,f,g,h = symbols("a,b,c,d,e,f,g,h", integer=True)
ecu = diophantine(200*a +100*b +50*c +20*d +10*e +5*f +2*g +h -200)


# =============================================================================
# HINT FIBONACCI
# =============================================================================
def fibo():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

# =============================================================================
# HINT DIVISORES
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


# =============================================================================
# HINT PITHAGORIC TRIPLET
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
    """
    Generador de tripletes pitagoricos
    """

    m = 1
    n = 2
    while True:
        if m == n:
            m = 1
            n += 1
        yield triplet(m, n)
        m += 1


# =============================================================================
# HINT BINOMIALS
# =============================================================================

from math import factorial as f
def b(m,n):
    return int(f(m)/(f(n)*f(m-n)))

# =============================================================================
# HINT SQUARE
# =============================================================================
def is_square(num):
     return num**0.5 % 1 == 0
