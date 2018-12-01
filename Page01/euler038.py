#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 38
        Take the number 192 and multiply it by each of 1, 2, and 3:
        192 × 1 = 192
        192 × 2 = 384
        192 × 3 = 576
        By concatenating each product we get the 1 to 9 pandigital, 192384576.
        We will call 192384576 the concatenated product of 192 and (1,2,3)

        The same can be achieved by starting with 9 and multiplying
        by 1, 2, 3, 4, and 5, giving the pandigital, 918273645,
        which is the concatenated product of 9 and (1,2,3,4,5).

        What is the largest 1 to 9 pandigital 9-digit number that can be
        formed as the concatenated product of an integer with
        (1,2, ... , n) where n > 1?
"""
# =============================================================================
# (upper left label is the current label)
#
# SOLUTION: 932718654
#
# STATUS: [ok]
# VERIFIED: [ok]
# EXECUTION TIME: [ok]
# =============================================================================

def euler38():
    result_list=[]
    repeated_char=False
    #
    for i in range(1,10000):
        num_list=[]
        for j in range(1,10):
            if repeated_char == False:
    #            print(" ",i, j, i*j)
                cad = str(i*j)
                #si hay un cero en la tupla, fuera
                if '0' in cad:
    #                print(i, j, "no vale porque sale 0")
                    break
                for char in cad:
                    #si hay un repetido en la lista, fuera
                    if char in num_list:
                        repeated_char = True
    #                    print(i,"no vale porque repite ", char)
                        break
                    num_list.append(char)
                if len(num_list) == 9 and repeated_char == False:
#                    print("FOUND", i, j, num_list)
                    result_list.append(int("".join(num_list)))
                    break
        repeated_char=False
    return(max(result_list))


if __name__ == "__main__":
    print(euler38())
    #932718654
