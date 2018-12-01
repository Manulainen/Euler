#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 42
        The nth term of the sequence of triangle numbers is given by,
        tn = ½n(n+1); so the first ten triangle numbers are:
        1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

        By converting each letter in a word to a number corresponding to its
        alphabetical position and adding these values we form a word value.
        For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
        If the word value is a triangle number then we shall
        call the word a triangle word.

        Using words.txt (right click and 'Save Link/Target As...'),
        a 16K text file containing nearly two-thousand common English words,
        how many are triangle words?
"""
# =============================================================================
# (upper left label is the current label)
#
# SOLUTION: 162
#
# STATUS: [ok]
# VERIFIED: [ok]
# EXECUTION TIME: [ok]
# =============================================================================

import string
UPPER_ASCII = string.ascii_uppercase


def generate_tnumber():
    num=1
    while True:
        ret = (num*(num+1))/2
        num +=1
        yield int(ret)

def get_char_pos(list_ascii, char):
    return list_ascii.index(char) + 1

def get_name_score(list_ascii, name):
    score = 0
    for letter in name:
        score += get_char_pos(list_ascii, letter)
    return score


def get_file_score():
    word_list = []
    with open("p042_words.txt") as fhand:
        for line in fhand:
            word_list = line.replace("\"", "").split(",")
    return word_list


def euler42():
    triangle_number_gen = generate_tnumber()
    triangle_list = []
    list_number = 0
    tWordCount = 0
    for word in get_file_score():
        #isTWord=False
        word_score =  get_name_score(UPPER_ASCII, word)

        while list_number <= word_score:
            list_number = next(triangle_number_gen)
            triangle_list.append(list_number)
        if word_score in triangle_list:
            #isTWord = True
            tWordCount +=1
            #print("{}\t\t{}\t {}".format(word, word_score, tWordCount))
    return tWordCount


if __name__ == "__main__":
    print(euler42())
    # 162
