#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 22
        Using names.txt (right click and 'Save Link/Target As...'),
        a 46K text file containing over five-thousand first names,
        begin by sorting it into alphabetical order. Then working out the
        alphabetical value for each name, multiply this value by its
        alphabetical position in the list to obtain a name score.

        For example, when the list is sorted into alphabetical order,
        COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
        is the 938th name in the list.
        So, COLIN would obtain a score of 938 × 53 = 49714.

        What is the total of all the name scores in the file?

"""
# =============================================================================
# (upper left label is the current label)
#
# SOLUTION: 871198282
#
# STATUS: [ok]
# VERIFIED: [ok]
# EXECUTION TIME: [ok]
# =============================================================================

import string

def get_char_pos(list_ascii, char):
    return list_ascii.index(char) + 1

def get_name_score(list_ascii, name):
    score = 0
    for letter in name:
        score += get_char_pos(list_ascii, letter)
    return score


def euler22():
    UPPER_ASCII = string.ascii_uppercase
    with open("p022_names.txt") as fhand:
        for line in fhand:
            list_names = line.replace("\"", "").split(",")
    list_names = sorted(list_names)

    total_scores = 0
    for index, name_score in enumerate(list_names, 1):
        #print(index, name_score, get_name_score(UPPER_ASCII, name_score),
        #      index*get_name_score(UPPER_ASCII, name_score))
        total_scores += index * get_name_score(UPPER_ASCII, name_score)
    return total_scores


if __name__ == "__main__":
    print(euler22())
    # 871198282
