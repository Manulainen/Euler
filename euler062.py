#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 062
        The cube, 41063625 (345^3), can be permuted to produce two other cubes:
        56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the
        smallest cube which has exactly three permutations of its digits
        which are also cube.

        Find the smallest cube for which exactly
        five permutations of its digits are cube.
"""
# =============================================================================
# (upper left label is the current label)
#
# SOLUTION: 127035954683
#
# STATUS: [ok]
# VERIFIED: [no/ok]
# EXECUTION TIME: [ok]
# =============================================================================

# Remove if not necessary
# import sys
# sys.path.append('../../')
# from Euler.EulerUtils import eulerFunctions as ef


# para cada cubo, inserto en un diccionario:
# clave el cubo con cifras ordenadas 6^3 =216 => 126
# valor frecuencia con la que ha salido la clave ordenada
# Al llegar a 5 miro en otro diccionario quien fue el primer valor en insertarlo

def euler062(numero_repeticiones):
    diccionario_frecuencias={}
    c={}
    i=0
    while numero_repeticiones not in diccionario_frecuencias.values():
        i+=1

        #Una tupla puede ser un indice para un diccionario
        listaOrdenadaCubo = tuple(sorted(str(i**3)))

        diccionario_frecuencias[listaOrdenadaCubo] = (1
                        + diccionario_frecuencias.get(listaOrdenadaCubo,0))

        # Para cada tupla ordenada nueva, creo un diccionario
        # la clave es la tupla
        #el valor una lista de los indices que generan ese cubo ordenado
        if listaOrdenadaCubo not in c.keys():
    	    c[listaOrdenadaCubo] = []
        c[listaOrdenadaCubo].append(i)
    return(c[listaOrdenadaCubo][0]**3)


if __name__ == "__main__":
    print(euler062(3))
    # 4106325
    print(euler062(5))
    # 127035954683
