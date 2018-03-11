#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 19
        You are given the following information,
        but you may prefer to do some research for yourself.
        1 Jan 1900 was a Monday.
        Thirty days has September,
        April, June and November.
        All the rest have thirty-one,
        Saving February alone,
        Which has twenty-eight, rain or shine.
        And on leap years, twenty-nine.
        A leap year occurs on any year evenly divisible by 4,
        but not on a century unless it is divisible by 400.

        How many Sundays fell on the first of the month during the
        twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

# =============================================================================
# [resuelto] 171
# [comprobado]
# =============================================================================

from math import floor

def zeller_congruence(q, m, k, j):
    """
    devuelve el dia de la semana de una fecha concreta.
    Los meses van de 3 marzo a 14 febrero.
    los dias de sabado 0 a viernes 6
    """
    h = (q+floor((13*(m+1))/5) + k + floor(k/4) + floor(j/4) - 2*j)%7
    return h

def euler19():
    """
    Calcula numero de domingos entre [1901-2000] que caen en 1 de mes
    """
    num_sun = 0

    # de 1901 a 2000
    #
    for year in range(1901, 2000+1):
        j = int(str(year)[:2])
        k = int(str(year)[2:])

        # el anio anterior a 00 es el 99
        # para el resto es anio -1
        #
        if k == 0:
            kminus = 99
        else:
            kminus = k-1

        # Enero 13 Febrero 14 del anio anterior
        #
        for month in range(13, 14+1):
            day = zeller_congruence(1, month, kminus, j)
            if day == 1:
                num_sun += 1

        # Marzo 3 Diciembre 12 del anio en curso
        #
        for month in range(3, 12+1):
            day = zeller_congruence(1, month, k, j)
            if day == 1:
                num_sun += 1

    return num_sun

if __name__ == "__main__":
    print(euler19())
    # 171
