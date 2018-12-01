#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 20
        n! means n × (n − 1) × ... × 3 × 2 × 1
            For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
            and the sum of the digits in the number 10! is
            3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

            Find the sum of the digits in the number 100!
"""
# =============================================================================
# (upper left label is the current label)
#
# SOLUTION: 648
#
# STATUS: [ok]
# VERIFIED: [ok]
# EXECUTION TIME: [ok]
# =============================================================================

from math import factorial as f

def euler20(big_num):
        return sum((int(x) for x in list(str(f(big_num)))))


if __name__ == "__main__":
    print(euler20(10))
    # 27
    print(euler20(100))
    # 648
