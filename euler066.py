#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 066
        Consider quadratic Diophantine equations of the form:
            x^2 – Dy^2 = 1

        For example, when D=13, the minimal solution in x is 649^2 – 13×180^2 = 1.
        It can be assumed that there are no solutions in positive
        integers when D is square.
        By finding minimal solutions in x for D = {2, 3, 5, 6, 7},
        we obtain the following:

            3^2 – 2×2^2 = 1
            2^2 – 3×1^2 = 1
           *9^2 – 5×4^2 = 1
            5^2 – 6×2^2 = 1
            8^2 – 7×3^2 = 1

        Hence, by considering minimal solutions in x for D = 7,
        the largest x is obtained when D=5.

        Find the value of D = 1000 in minimal solutions of x for which
        the largest value of x is obtained.
"""
# =============================================================================
# (upper left label is the current label)
#
# SOLUTION: 661
#
# STATUS: [ok]
# VERIFIED: [ok]
# EXECUTION TIME: [long/ok]
# =============================================================================

import sys
sys.path.append('../')
sys.path.append('../../')
from Euler.EulerUtils import eulerFunctions as ef

#OLD Approach, neckbottle wih 13, 29...
#Recorre D, recorre X y recorre de modo invertido y.
#top = 7
#square_list = [x**2 for x in range(top+1)]
#for D in range(top+1):
#    if D not in square_list:
#        x = 0
#        found = False
#        while found is False:
#            x += 1
#            for y in reversed(range(x+1)):
#                if x**2 - D*y**2 == 1:
#                    if x > 0 and y > 0:
#                        print("{}^2 - {}x{}^2 = 1".format(x,D,y))
#                        found = True
#                        break

#Old approach, para cada x, miro si y despejada tiene raiz (asi no la recorro)
#Recorre D, busca si x tiene solucion, resuelve y
#top = 4
#for D in range(top+1):
#    if not is_square(D):
#       # print("A ", D)
#        x = 0
#        found = False
#        while found is False:
#            x += 1
#            #print("B ",D, x)
#            y = (1-x**2) / (-D)
#            if x > 0 and y > 0:
#                if is_square(y):
#                    y = int(sqrt(y))
#                    print("{}^2 - {}x {}^2 = 1".format(x,D,y))
#                    found = True
#                    break


from sympy.solvers.diophantine import diop_DN

def euler066(top):
    maxX = 0
    for D in range(top+1):
        if not ef.is_square(D):
            solution = diop_DN(D,1)
            x= solution[0][0]
           # y= solution[0][1]
           # print("{}^2 - {}x {}^2 = 1".format(x, D, y))
            if x > maxX:
                maxX = x
                maxTuple = x,D
    return maxTuple[1]

if __name__ == "__main__":
    print(euler066(7))
    # 5
    print(euler066(13))
    # 13
    print(euler066(1000))
    # 661
