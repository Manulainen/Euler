 #!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 17
        If the numbers 1 to 5 are written out in words:
        one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
        letters used in total.

        If all the numbers from 1 to 1000 (one thousand) inclusive were
        written out in words, how many letters would be used?

        NOTE: Do not count spaces or hyphens. For example,
        342 (three hundred and forty-two) contains 23 letters and
        115 (one hundred and fifteen) contains 20 letters.
        The use of "and" when writing out numbers is in compliance
        with British usage.
"""

# =============================================================================
# [resuelto] 21124
# [comprobado]
# =============================================================================

ordinalDict = {}
ordinalDict[1] = "one"
ordinalDict[2] = "two"
ordinalDict[3] = "three"
ordinalDict[4] = "four"
ordinalDict[5] = "five"
ordinalDict[6] = "six"
ordinalDict[7] = "seven"
ordinalDict[8] = "eight"
ordinalDict[9] = "nine"

ordinalDict[10] = "ten"
ordinalDict[11] = "eleven"
ordinalDict[12] = "twelve"
ordinalDict[13] = "thirteen"
ordinalDict[14] = "fourteen"
ordinalDict[15] = "fifteen"
ordinalDict[16] = "sixteen"
ordinalDict[17] = "seventeen"
ordinalDict[18] = "eighteen"
ordinalDict[19] = "nineteen"

ordinalDict[20] = "twenty"
ordinalDict[30] = "thirty"
ordinalDict[40] = "forty"
ordinalDict[50] = "fifty"
ordinalDict[60] = "sixty"
ordinalDict[70] = "seventy"
ordinalDict[80] = "eighty"
ordinalDict[90] = "ninety"

ordinalDict[100] = "hundred"
ordinalDict[1000] = "onethousand"

# 20 ... 99
def traduceDecenas(numero):
    if numero == 0:
        return ""
    elif numero < 21:
        return ordinalDict[numero]
    else:
        if numero % 10 == 0:
            return ordinalDict[numero]
        else:
         cad = ordinalDict[(numero // 10) * 10]
         return cad + ordinalDict[numero % 10]

# 100, 200, 300, 400 ... 900
def traduceCentenas(numero):
    if numero / 100 == 1:
        cad = ordinalDict[1]
    else:
        cad = ordinalDict[numero / 100]
    return cad + ordinalDict[100]

def decompose(number):
    if number == 1000:
        return ordinalDict[number]
    if number<100:
        return traduceDecenas(number)
    else:
        cent = traduceCentenas((number//100)*100)
        decenas = traduceDecenas(number - (number//100)*100)
        if decenas == "":
            return cent
        else:
            return cent + "and" + decenas

def euler17(top):
    counter = 0
    for i in range(1,top+1):
        #print(i, decompose(i), len(decompose(i)))
        counter += len(decompose(i))
    return counter

if __name__ == "__main__":
    print(euler17(5))
    #19
    print(euler17(1000))
    #21124

