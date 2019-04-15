#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 067
        By starting at the top of the triangle below and moving to adjacent
        numbers on the row below, the maximum total from top to bottom is 23.

            3
           7 4
          2 4 6
         8 5 9 3

        That is, 3 + 7 + 4 + 9 = 23.

        Find the maximum total from top to bottom in triangle.txt
        (right click and 'Save Link/Target As...'), a 15K text file
        containing a triangle with one-hundred rows.

        NOTE: This is a much more difficult version of Problem 18.
        It is not possible to try every route to solve this problem,
        as there are 299 altogether! If you could check one trillion (1012)
        routes every second it would take over twenty billion years to check
        them all. There is an efficient algorithm to solve it. ;o)
"""
# =============================================================================
# (upper left label is the current label)
#
# SOLUTION: 7273
#
# STATUS: [ok]
# VERIFIED: [no/ok]
# EXECUTION TIME: [ok]
# =============================================================================

# Remove if not necessary
# import sys
# sys.path.append('../')
# sys.path.append('../../')
# from Euler.EulerUtils import eulerFunctions as ef

TLITTLE = [[3],
           [7, 4],
           [2, 4, 6],
           [8, 5, 9, 3]]


TBIG = []
with open('p067_triangle.txt') as fhand:
    for line in fhand:
        lint = [int(x) for x in line.strip().split(' ')]
        TBIG.append(lint)

def evaluate_row(piramid, row):
    """
    Pide total no la ruta.
    Dada una fila de la piramide, devuelve una nueva fila con los maximos de
    dos a dos

    old_row = [8, 5, 9, 3]

    max(8,5)->8
    max(5,9)->9
    max(9,3)->9

    new_row = [8, 9, 3]
    """
    new_row = []
    if row == 0:
        return row
    else:
        for i in range(len(piramid[row]) - 1):
            new_row.append(max(piramid[row][i], piramid[row][i+1]))
    return new_row

def euler067(piramid):
    """
    A cada fila le suma el evaluate_row de la fila siguiente
    (tienen la misma longitud)
    devuelve el pico de la piramide con todas las sumas
    """
    for i in range(len(piramid)-2, -1, -1):
        piramid[i] = [a + b for a, b in zip(piramid[i],
                                            evaluate_row(piramid, i+1))]
    return piramid[i][0]

if __name__ == "__main__":
    print(euler067(TLITTLE))
    #23
    print(euler067(TBIG))
    #7273
