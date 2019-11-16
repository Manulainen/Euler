#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 061
        Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal 
        numbers are all figurate (polygonal) numbers and are generated 
        by the following formulae:
        Triangle 	  	P3,n=n(n+1)/2 	  	1, 3, 6, 10, 15, ...
        Square 	    	P4,n=n2 	  	1, 4, 9, 16, 25, ...
        Pentagonal 	  	P5,n=n(3n−1)/2 	  	1, 5, 12, 22, 35, ...
        Hexagonal 	  	P6,n=n(2n−1) 	  	1, 6, 15, 28, 45, ...
        Heptagonal 	  	P7,n=n(5n−3)/2 	  	1, 7, 18, 34, 55, ...
        Octagonal 	  	P8,n=n(3n−2) 	  	1, 8, 21, 40, 65, ...

        The ordered set of three 4-digit numbers: 8128, 2882, 8281,
        has three interesting properties.

        The set is cyclic, in that the last two digits of each number is 
        the first two digits of the next number 
        (including the last number with the first).
        Each polygonal type: triangle (P3,127=8128), square (P4,91=8281), 
        and pentagonal (P5,44=2882), is represented by a different 
        number in the set.
        This is the only set of 4-digit numbers with this property.

        Find the sum of the only ordered set of six cyclic 4-digit numbers 
        for which each polygonal type: triangle, square, pentagonal, 
        hexagonal, heptagonal, and octagonal, is represented
        by a different number in the set.

"""
# =============================================================================
# (upper left label is the current label)
#
# SOLUTION: 28684
#
# STATUS: [ok]
# VERIFIED: [ok]
# EXECUTION TIME: [ok]
# =============================================================================

# Remove if not necessary
import sys
sys.path.append('../')
#sys.path.append('../../')
from Euler.EulerUtils import eulerFunctions as ef
import itertools

func_d={}
func_d[3] = ef.T
func_d[4] = ef.squa
func_d[5] = ef.P
func_d[6] = ef.H
func_d[7] = ef.hept
func_d[8] = ef.octo

di={}
def generate_lists(pol): 
    di[pol]=[]
    n = 1
    cond = True
    while cond:
        num = func_d[pol](n)
        if len(str(num)) == 4:
           di[pol].append((n,num))
        if len(str(num))>4   :
            cond = False
        n+=1
   
#Esto me genera un diccionario con 8 entradas con numeros de 4 cifras
for key in func_d.keys():
    generate_lists(key)


# Genera una lista de listas que son posibles paths a  mirar
# Empiezan y acaban en 3. Hay 120 en total
paths=[]
paths_t = itertools.permutations([4,5,6,7,8],5)
for path in paths_t:
    l =list(path)
    l.insert(0,3)
    paths.append(l)

def search_in_l(path):
    l1 = path[0]
    l2 = path[1]
    l3 = path[2]
    l4 = path[3]
    l5 = path[4]
    l6 = path[5]
    for na, a in di[l1]:
        car_a = str(a)[0:2]
        cdr_a = str(a)[2:4]
        for nb, b in di[l2]:
            car_b = str(b)[0:2]
            cdr_b = str(b)[2:4]
            if cdr_a == car_b:
                for nc, c in di[l3]:
                    car_c = str(c)[0:2]
                    cdr_c = str(c)[2:4]
                    if cdr_b == car_c:
                        for nd, d in di[l4]:
                            car_d = str(d)[0:2]
                            cdr_d = str(d)[2:4]
                            if cdr_c == car_d:
                                for ne, e in di[l5]:
                                    car_e = str(e)[0:2]
                                    cdr_e = str(e)[2:4]
                                    if cdr_d == car_e:
                                        for nf, f in di[l6]:
                                            car_f = str(f)[0:2]
                                            cdr_f = str(f)[2:4]
                                            if cdr_e == car_f and cdr_f == car_a:
#                                                print(a,b,c,d,e,f, 
#                                                       a+b+c+d+e+f,
#                                                       l1,l2,l3,l4,l5,l6,
#                                                       na,nb,nc,nd,ne,nf)
                                                return (True, a+b+c+d+e+f)
    return (False, 0)
                        
def euler061():
    for path in paths:
      found, value = search_in_l(path)
      if found:
          return value

if __name__ == "__main__":
    print(euler061())
    # 28684
