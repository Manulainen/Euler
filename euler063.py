#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 063
        The 5-digit number, 16807=7^5, is also a fifth power.
        Similarly, the 9-digit number, 134217728=8^9, is a ninth power.
        How many n-digit positive integers exist which are also an nth power?
"""
# =============================================================================
# (upper left label is the current label)
#
# SOLUTION: 49
#
# STATUS: [ok]
# VERIFIED: [ok]
# EXECUTION TIME: [ok]
# =============================================================================

# Remove if not necessary
# import sys
# sys.path.append('../../')
# from Euler.EulerUtils import eulerFunctions as ef

#a^b  cuando b == len(a^^b)
#a esta acotado del 1 al 10 porque 10^1 = 10
#el numero siempre sera mayor que el exponente
#b esta acotado mas o menos del 1 al 20 o asi, esto se comprueba en un bucle.
#Vale la pena dejar la grafica como ejemplo

#import matplotlib.pyplot as plt
#base crece exponencial
#longitud crece lineal

#base=[]
#length=[]
#a=1
#tot = 100
#for b in range(tot):
##b=1
##while b <=  len(str(a**b)) or b<100:
#    print("{}^{} es {}, [{}]len".format(a,b,a**b, len(str(a**b))))
#    base.append(b)
#    length.append(len(str(a**b)))
#    #b+=1
#
#plt.plot(range(len(base)),base, label="b")
#plt.plot(range(len(base)),length, label="length")
#plt.legend()

def euler063():
    found = 0
    for a in range(1,10):
        b = 1
        while b <= len(str(a**b)) or b<100: #Sanity check
            if b == len(str(a**b)):
#                print("{}^{} = {}, len = {}".format(a,b,a**b, len(str(a**b))))
                found += 1
            b += 1
    return found


if __name__ == "__main__":
    print(euler063())
    # 49
