#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 25
        The Fibonacci sequence is defined by the recurrence relation:
            Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

        Hence the first 12 terms will be:
        F1 = 1
        F2 = 1
        F3 = 2
        F4 = 3
        F5 = 5
        F6 = 8
        F7 = 13
        F8 = 21
        F9 = 34
        F10 = 55
        F11 = 89
        F12 = 144

        The 12th term, F12, is the first term to contain three digits.
        What is the index of the first term in the Fibonacci sequence
        to contain 1000 digits?

"""

# =============================================================================
# [resuelto] 4782
# [comprobado]
# =============================================================================

def fibo():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

def euler25():
    genera_fibo = enumerate(fibo(),1)
    len_fib_number = 0
    while len_fib_number < 1000:
        fib_index, fib_number = next(genera_fibo)
        len_fib_number = len(str(fib_number))
    return fib_index

if __name__ == "__main__":
    print(euler25())
    #4782
