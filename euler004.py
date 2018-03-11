#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 4
         A palindromic number reads the same both ways. The largest palindrome
         made from the product of two 2-digit numbers is 9009 = 91 × 99.
         Find the largest palindrome made from the product of
         two 3-digit numbers.
"""
# =============================================================================
# [resuelto] 906609
# [comprobado]
# =============================================================================
def pal(X):
    cad=str(X)
    if cad == cad[::-1]:
        return True
    return False

#def euler4a(max_range):
#    t=[]
#    for i in range(max_range+1):
#        for j in range(max_range+1):
##            print(i,j)
#            if(pal(i*j)):
#                t.append(i*j)
#    print("4a", len(t))
#    return(max(t))
#
#def euler4b(max_range):
#    t=[]
#    for i in range(1,max_range+1):
#        for j in range(1,max_range+1):
##            print(i,j)
#            if(pal(i*j)):
#                t.append(i*j)
#    print("4b", len(t))
#    return(max(t))


def euler4(max_range):
    t=[]
    for i in range(1,max_range+1):
        for j in range(i,max_range+1):
            if(pal(i*j)):
                t.append(i*j)
    return(max(t))


if __name__ == "__main__":
    print(euler4(99))
    # 9009
    print(euler4(999))
    #906609

