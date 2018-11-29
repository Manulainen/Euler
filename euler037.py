#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 37
        The number 3797 has an interesting property. Being prime itself,
        it is possible to continuously remove digits from left to right,
        and remain prime at each stage: 3797, 797, 97, and 7.
        Similarly we can work from right to left: 3797, 379, 37, and 3.

        Find the sum of the only eleven primes that are both truncatable
        from left to right and right to left.

        NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
# =============================================================================
# (upper left label is the current label)
#
# SOLUTION: 748317
#
# STATUS: [ok]
# VERIFIED: [ok]
# EXECUTION TIME: [long/ok]
# =============================================================================

from math import sqrt

def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True


def evaluate_chunks(prime, prime_list):

    #Evaluo si es par la rama izquierda y derecha. En el mismo bucle va el
    #mismo nivel de rama izq y der.
    for i in range(1, len(str(prime))):
        if not is_prime(int(str(prime)[:i])) or not is_prime(int(str(prime)[i:])):
               return None

    prime_list.append(prime)
    #print("[{}], {}".format(len(prime_list), prime))



#Empiezo en 2 digitos
def generate_prime():
    j=10
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

def euler37():
    it = generate_prime()
    prime_list = []
    while len(prime_list) < 11:
        prime = next(it)

        #Si en la lista hay un par, no sigo evaluando
        list_number = list(str(prime))
        for i in list_number:
            if(int(i) % 2 == 0):
                continue
        evaluate_chunks(prime, prime_list)
    return sum(prime_list)

if __name__ == "__main__":
    print(euler37())
    # 748317
