#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 14
        The following iterative sequence is defined
        for the set of positive integers:
            n → n/2 (n is even)
            n → 3n + 1 (n is odd)

        Using the rule above and starting with 13,
        we generate the following sequence:
            13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

        It can be seen that this sequence (starting at 13 and finishing at 1)
        contains 10 terms. Although it has not been proved yet
        (Collatz Problem), it is thought that all starting numbers finish at 1.

        Which starting number, under one million, produces the longest chain?
        NOTE: Once the chain starts the terms are
        allowed to go above one million.
"""
# =============================================================================
# [resuelto] 837799
# [comprobado]
# =============================================================================

import time


# =============================================================================
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# =============================================================================

def startsequence(big_number, lst, it=1):
    lst.append(big_number)
    if big_number == 1:
        return it
    else:
        if big_number % 2 == 0:
            return startsequence(int(big_number / 2), lst, it + 1)
        else:
            return startsequence(int(3 * big_number + 1), lst, it + 1)

#t1=time.clock()
#for i in range(1,1000000):
#    startsequence(i)
#    #print(i, startsequence(i))
#t2=time.clock()
#print("Elapsed", t2-t1)


# =============================================================================
#def internalgetCollatzNumber(big_number, d={}, it=1):
#    """
#    Verifica en un diccionario si existe una entrada para alguno de sus
#    hijos, si lo encuentra, suma sus it a estos y corta la ejecucion, ahorrando
#    muchos pasos
#    """
#    if big_number in d:
#        #print("found! {}, me ahorro {}".format(big_number,d.get(big_number)))
#        return it + d.get(big_number)-1
#    else:
#        if big_number == 1:
#            return it
#        else:
#            if big_number % 2 == 0:
#                return internalgetCollatzNumber(
#                    int(big_number / 2), d, it + 1)
#            else:
#                return internalgetCollatzNumber(
#                    int(3 * big_number + 1), d, it + 1)

def getCollatzNumber(big_number, d=dict(), it=1):
    """
    Verifica en un diccionario si existe una entrada para alguno de sus
    hijos, si lo encuentra, suma sus it a estos y corta la ejecucion, ahorrando
    muchos pasos
    """
    if big_number in d:
        #print("found! {}, me ahorro {}".format(big_number,d.get(big_number)))
        return it + d.get(big_number)-1

    if big_number == 1:
        return it
    if big_number % 2 == 0:
        return getCollatzNumber(
            int(big_number / 2), d, it + 1)
    return getCollatzNumber(
        int(3 * big_number + 1), d, it + 1)

#def getCollatzNumber(big_number, d):
#    num_steps = internalgetCollatzNumber(big_number, d, it=1)
#    d[big_number] = num_steps
#    #print(big_number, num_steps)
#    return (big_number, num_steps)

#a1 = time.clock()
#d = {}
#maxT = 0, 0
#for i in range(1, 1000000, 1): # en el tercer argumento esta la optimizacion...
#    result = getCollatzNumber(i, d)
#    if result[1] > maxT[1]:
#        maxT = result
#print(maxT)
#    #print("FINAL: {} tiene {} saltos".format(i, a(i, d)))
#b1 = time.clock()
#print("Elapsed", b1 - a1)

def euler14(big_number):
    d = {}
    maxT = 0, 0
    for i in range(1, big_number, 1): # en el tercer argumento esta la optimizacion...
        num_steps = getCollatzNumber(i, d)
        d[i] = num_steps
        #print(big_number, num_steps)
        result = i, num_steps
        #result = getCollatzNumber(i, d)
        if result[1] > maxT[1]:
            maxT = result
    return(maxT[0])
        #print("FINAL: {} tiene {} saltos".format(i, a(i, d)))

# =============================================================================

if __name__ == "__main__":
    t1 = time.clock()
    print(euler14(1000000))
    #(837799, 525)
    t2 = time.clock()
    print("Elapsed", t2 - t1)





#import numpy as np
#x = np.arange(50,100)
#
#y = []
#for i in x:
#    y.append(startsequence(i))
#y = np.array(y)
#
#import matplotlib.pyplot as plt
#
#plt.xticks(x)
#plt.grid(axis="x")
#plt.plot(x, y)


#
#plist = [27,31,41,47,54,55,62,63,71,73,82,83,91,94,95,97]
#
#for x in plist:
#    t = []
#    startsequence(x,t)
#    print("x{} = {}".format(x,t))
#    print()

