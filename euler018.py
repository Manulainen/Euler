#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 18
        By starting at the top of the triangle below and moving to
        adjacent numbers on the row below, the maximum total from
        top to bottom is 23.

        3
        7 4
        2 4 6
        8 5 9 3

        That is, 3 + 7 + 4 + 9 = 23.

        Find the maximum total from top to bottom of the triangle below:

        75
        95 64
        17 47 82
        18 35 87 10
        20 04 82 47 65
        19 01 23 75 03 34
        88 02 77 73 07 63 67
        99 65 04 28 06 16 70 92
        41 41 26 56 83 40 80 70 33
        41 48 72 33 47 32 37 16 94 29
        53 71 44 65 25 43 91 52 97 51 14
        70 11 33 28 77 73 17 78 39 68 17 57
        91 71 52 38 17 14 91 43 58 50 27 29 48
        63 66 04 68 89 53 67 30 73 16 69 87 40 31
        04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

        NOTE: As there are only 16384 routes, it is possible to solve
        this problem by trying every route. However, Problem 67, is the
        same challenge with a triangle containing one-hundred rows;
        it cannot be solved by brute force, and requires a clever method! ;o)
"""

# =============================================================================
# [resuelto] 1074
# [comprobado]
# =============================================================================

TLITTLE = [[3],
           [7, 4],
           [2, 4, 6],
           [8, 5, 9, 3]]


TBIG = [[75],
        [95, 64],
        [17, 47, 82],
        [18, 35, 87, 10],
        [20,  4, 82, 47, 65],
        [19,  1, 23, 75,  3, 34],
        [88,  2, 77, 73,  7, 63, 67],
        [99, 65,  4, 28,  6, 16, 70, 92],
        [41, 41, 26, 56, 83, 40, 80, 70, 33],
        [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
        [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
        [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
        [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
        [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
        [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]]


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

def euler18(piramid):
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
    print(euler18(TLITTLE))
    #23
    print(euler18(TBIG))
    #1074
