#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 071
        Consider the fraction, n/d, where n and d are positive integers. 
        If n<d and HCF(n,d)=1, it is called a reduced proper fraction.
        If we list the set of reduced proper fractions 
        for d ≤ 8 in ascending order of size, we get:

        1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 
        4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

        It can be seen that 2/5 is the fraction immediately to the left of 3/7.
        By listing the set of reduced proper fractions for d ≤ 1,000,000 in 
        ascending order of size, find the numerator of the fraction 
        immediately to the left of 3/7.

"""
# =============================================================================
# (upper left label is the current label)
#
# SOLUTION: 428570
#
# STATUS: [ok]
# VERIFIED: [ok]
# EXECUTION TIME: [ok]
# =============================================================================

# Remove if not necessary
# import sys
# sys.path.append('../')
# sys.path.append('../../')
# from Euler.EulerUtils import eulerFunctions as ef
import fractions

def calcula_N():
    N = 1
    # funcion escalera
    # sube 1 peldaño y aguanta 3 ciclos
    # sube 1 peldaño y aguanta 2 ciclos
    # sube 1 peldaño y aguanta 2 ciclos
    #vuelta a empezar
    while (True):
        for i in range(7):
            if i == 0:
                N+=1
            if i == 3:
                N+=1
            if i == 5:
                N+=1
            
            yield N

def euler071(top):
    fracMin = fractions.Fraction(2,5)
    fracTop = fractions.Fraction(3,7)
    
    #l as fracciones iran con denominador de 5 al tope, el resto se descarta
    # es una pequeña poda.
    #probablemente en este punto se pueda hacer una poda importante,
    #pero el resultado ya se obtiene suficientemente rapido
    n_gen = calcula_N()
    for i in range(5, top+1):
        #Aqui necesito una lógica que me diga a partir de quien calculo la j, 
        # eso hará una increíble poda por la izquierda
        N = next(n_gen)
        for j in range(N, i):
            frac = fractions.Fraction(j,i)
            if frac >= fracTop:
                #Poda por la derecha, estos de aqui no me interesan, son mayores o igual al tope.
                break
                print("\033[31m {}/{} --> {}/{}\033[0m".format(j,i, frac.numerator, frac.denominator))
            else:
                #De estos me interesa exactamente el último antes del break!
    #            print("{}/{} --> {}/{}".format(j,i, frac.numerator, frac.denominator))
    
                #En este punto con poda, por cada iteracion obtengo unicamente una 
                #fraccion, que es la inmediatamente inferior a 3/7.
                # asi que no necesito un diccionario, sino un único valor que vaya almacenando
                #la fraccion mayor
    #            d[(frac.numerator, frac.denominator)] = frac
                if frac > fracMin:
                    fracMin = frac
                    
    return fracMin
   
    



if __name__ == "__main__":
    print(euler071(8))
    # 2/5
    print(euler071(1000000))
    # 428570/999997