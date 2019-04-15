#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 069
        Euler's Totient function, φ(n) [sometimes called the phi function],
        is used to determine the number of numbers less than n which are
        relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8,
        are all less than nine and relatively prime to nine, φ(9)=6.

    n 	Relatively Prime 	φ(n) 	n/φ(n)
    2 	1                   1       2
    3 	1,2 	            2    	1.5
    4 	1,3 	            2 	    2
    5 	1,2,3,4 	        4 	    1.25
    6 	1,5 	            2    	3
    7 	1,2,3,4,5,6 	    6 	    1.1666...
    8 	1,3,5,7 	        4 	    2
    9 	1,2,4,5,7,8 	    6 	    1.5
    10 	1,3,7,9 	        4 	    2.5

        It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.
        Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
"""
# =============================================================================
# (upper left label is the current label)
#
# SOLUTION: 510510
#
# STATUS: [ok]
# VERIFIED: [no/ok]
# EXECUTION TIME: [long]
# =============================================================================

# Remove if not necessary
import sys
sys.path.append('../')
# sys.path.append('../../')
from Euler.EulerUtils import eulerFunctions as ef
from math import gcd


PHI_D = {1:1}
QUO_D = {1:1}

def get_phi_mn(m,n):
    d = gcd(m,n)
    return int(PHI_D[m]*PHI_D[n]* (d / PHI_D[d]))

def euler069(top):
    maxVal = 0,0
    for n in range(2, top):

        # En el diccionario sólo voy a ir guardando los PHIS
        # Si N es primo, su phi es n-1 ya que todos los elementos antes que el son coprimos
        if ef.is_prime(n):
            #print("N:{} prime, φ({})={}".format(n, n, n-1))
            PHI_D[n] = n-1
            QUO_D[n] = n / (n-1)

        else:
            nAux = n
            pgen = ef.generate_prime(2)

            while nAux != 1:
                prime = next(pgen)
                if nAux%prime == 0:
                    phi = get_phi_mn(prime, int(nAux/prime))
                   # print("N:{} = {}.{} φ({})={}".format(n, prime, int(nAux/prime), n, phi))
                    PHI_D[n] = phi
                    QUO_D[n] = n / phi


                    if QUO_D[n] > maxVal[1]:
                        maxVal = n, QUO_D[n]

                    break
    return maxVal
    #print("MaxVal encontrado: ", maxVal)

if __name__ == "__main__":
    pass
    print(euler069(10))
    # 6
    print(euler069(1000000))
    # 510510
