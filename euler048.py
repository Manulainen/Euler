#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 48
        The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
        Find the last ten digits of the series,
        1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""
# =============================================================================
# (upper left label is the current label)
#
# SOLUTION: 9110846700
#
# STATUS: [ok]
# VERIFIED: [ok]
# EXECUTION TIME: [ok]
# =============================================================================

def euler48(top):
    return str(sum((x**x for x in range(1,top+1))))[-10:]

if __name__ == "__main__":
    print(euler48(10))
    # 0405071317
    print(euler48(1000))
    # 9110846700
