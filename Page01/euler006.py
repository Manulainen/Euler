#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 6
        The sum of the squares of the first ten natural numbers is,
        1² + 2² + ... + 10² = 385

        The square of the sum of the first ten natural numbers is,
        (1 + 2 + ... + 10)² = 3025

        Hence the difference between the sum of the squares of the first
        ten natural numbers and the square of the sum is 3025 − 385 = 2640.
        Find the difference between the sum of the squares of the first
        one hundred natural numbers and the square of the sum.
"""
# =============================================================================
# (upper left label is the current label)
#
# SOLUTION: 25164150
#
# STATUS: [ok]
# VERIFIED: [ok]
# EXECUTION TIME: [ok]
# =============================================================================

def sum_of_squares(top):
    """
    1² + 2² + ... + top²
    """

    return (top * (top + 1) * (2 * top + 1)) / 6

def square_of_sum(top):
    """
    (1 + 2 + ... + top)²
    """

    return ((top * (top + 1)) / 2) ** 2

def euler6(top):
    """
    (1 + 2 + ... + top)² - (1² + 2² + ... + top²)
    """

    return int(square_of_sum(top) - sum_of_squares(top))


if __name__ == "__main__":
    print(euler6(10))
#385
    print(euler6(100))
#25164150
