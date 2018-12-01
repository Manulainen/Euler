#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 47
        The first two consecutive numbers to have
        two distinct prime factors are:
        14 = 2 × 7
        15 = 3 × 5

        The first three consecutive numbers to have
        three distinct prime factors are:
        644 = 2² × 7 × 23
        645 = 3 × 5 × 43
        646 = 2 × 17 × 19.

        Find the first four consecutive integers to have
        four distinct prime factors each. What is the first of these numbers?
"""
# =============================================================================
# (upper left label is the current label)
#
# SOLUTION: 134043
#
# STATUS: [ok]
# VERIFIED: [ok]
# EXECUTION TIME: [unacceptable/long/ok]
# =============================================================================

from eulerFunctions import get_prime_factors

def euler47(number_of_consecutive):
    """
    2 minutazos...
    """
    found = 0
    i=1
    while True:
        i+=1
        num_factors = len(get_prime_factors(i))
#        print(i, num_factors)
        if number_of_consecutive == num_factors:
            found += 1
            #print("***", i, len(get_prime_factors(i)), found)
            if found == number_of_consecutive:
#                print(i-number_of_consecutive +1, get_prime_factors(i-number_of_consecutive +1))
                return (i-number_of_consecutive +1)
        else:
            found = 0



if __name__ == "__main__":
    print(euler47(2))
    # 14
    print(euler47(3))
    # 644
    print(euler47(4))
    # 134043
