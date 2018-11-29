#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 31
        In England the currency is made up of pound, £, and pence, p,
        and there are eight coins in general circulation:

        1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
        It is possible to make £2 in the following way:
        1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

        How many different ways can £2 be made using any number of coins?
"""
# =============================================================================
# (upper left label is the current label)
#
# SOLUTION: 73682
#
# STATUS: [ok]
# VERIFIED: [ok]
# EXECUTION TIME: [ok]
# =============================================================================

# =============================================================================
#  1 Brute Force
# =============================================================================
def brute_force(total):
    numComb=0
    normalCount = 0
    for two in range(0, int(total/200)+1):
        for one in range(0, int(total/100)+1):
            for fiftyCent in range(0, int(total/50)+1):
                for twentyCent in range(0, int(total/20)+1):
                    for tenCent in range(0, int(total/10)+1):
                        for fiveCent in range(0, int(total/5)+1):
                            for twoCent  in range(0, int(total/2)+1):
                                oneCent = max(total -two*200-one*100
                                              -fiftyCent*50
                                              -twentyCent*20
                                              -tenCent*10
                                              -fiveCent*5
                                              -twoCent*2,0)
                                normalCount += 1

#                                print(two,one, fiftyCent, twentyCent, tenCent, fiveCent, twoCent, oneCent, " -->",
#                                      two*200+ one*100 + fiftyCent*50+ twentyCent*20+tenCent*10+fiveCent*5+twoCent*2+oneCent)
                                #print(tenCent, fiveCent, twoCent, oneCent, "-->", tenCent*10 + fiveCent*5 + twoCent*2 + oneCent)
                                if(two*200 +one*100 +fiftyCent*50
                                   +twentyCent*20 +tenCent*10 +fiveCent*5
                                   +twoCent*2 +oneCent == total):
                                    numComb += 1
#                                    print("xxxxxxxxxxxx")

                                elif(two*200 +one*100 +fiftyCent*50
                                   +twentyCent*20 +tenCent*10 +fiveCent*5
                                   +twoCent*2 +oneCent > total):
                                    break
                                    #print(fiveCent, twoCent, oneCent, "-->",fiveCent*5 + twoCent*2 + oneCent)
                                    #print(two,one, fiftyCent, twentyCent, tenCent, fiveCent, twoCent, oneCent, " -->",
                                    #      two*200+ one*100 + fiftyCent*50+ twentyCent*20+tenCent*10+fiveCent*5+twoCent*2+oneCent)

    #print("{}/{} ({}%)".format(numComb, normalCount, numComb/normalCount*100))
    return numComb

# =============================================================================
# 2 Brute Force Optimized
# =============================================================================
def euler31():
    total=200
    ways = 0
    for two in range(total, 0-1, -total):
        for one in range(two, 0-1, -int(total/2)):
            for fiftyCent in range(one, 0-1, -int(total/4)):
                for twentyCent in range(fiftyCent, 0-1, -int(total/10)):
                    for tenCent in range(twentyCent, 0-1,-int(total/20)):
                        for fiveCent in range(tenCent, 0-1,-int(total/40)):
                            for twoCent  in range(fiveCent, 0-1,-int(total/100)):
                                #print(two,one, fiftyCent, twentyCent, tenCent, fiveCent, twoCent, ways)
                                ways+=1
    return ways


#from sympy.solvers.diophantine import diophantine
#from sympy import symbols
#
#
#15x+21y=261
#a,b,c,d,e,f,g,h,z = symbols("a,b,c,d,e,f,g,h,z", integer=True)
#ecu = diophantine(200*a +100*b +50*c +20*d +10*e +5*f +2*g +h -200)
#
#{(t_0,
#  t_0 + t_1,
#  t_0 + t_1 + t_2,
#  t_0 + t_1 + t_2 + t_3,
#  t_0 + t_1 + t_2 + t_3 + t_4,
#  t_0 + t_1 + t_2 + t_3 + t_4 + t_5,
#  t_0 + t_1 + t_2 + t_3 + t_4 + t_5 + t_6,
#  -387*t_0 - 187*t_1 - 87*t_2 - 37*t_3 - 17*t_4 - 7*t_5 - 2*t_6 + 200)}


if __name__ == "__main__":
    print(euler31())
    #73682
