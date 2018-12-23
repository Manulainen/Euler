#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 059
        Each character on a computer is assigned a unique code and the
        preferred standard is ASCII (American Standard Code for Information
        Interchange). For example, uppercase A = 65, asterisk (*) = 42, and
        lowercase k = 107.

        A modern encryption method is to take a text file,
        convert the bytes to ASCII, then XOR each byte with a given value,
        taken from a secret key. The advantage with the XOR function is that
        using the same encryption key on the cipher text, restores the plain
        text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

        For unbreakable encryption, the key is the same length as the plain
        text message, and the key is made up of random bytes.
        The user would keep the encrypted message and the encryption key
        in different locations, and without both "halves", it is impossible
        to decrypt the message.

        Unfortunately, this method is impractical for most users, so the
        modified method is to use a password as a key. If the password is
        shorter than the message, which is likely, the key is repeated
        cyclically throughout the message. The balance for this method is
        using a sufficiently long password key for security, but short
        enough to be memorable.

        Your task has been made easy, as the encryption key consists of
        three lower case characters. Using cipher.txt (right click and 'Save
        Link/Target As...'), a file containing the encrypted ASCII codes,
        and the knowledge that the plain text must contain common English
        words, decrypt the message and find the sum of the ASCII values
        in the original text.
"""
# =============================================================================
# (upper left label is the current label)
#
# SOLUTION: 107359
#
# STATUS: [ok]
# VERIFIED: [no/ok]
# EXECUTION TIME: [ok]
# =============================================================================

# Remove if not necessary
# import sys
# sys.path.append('../../')
# from Euler.EulerUtils import eulerFunctions as ef

###############################################################################
#
# Dictionary file from : https://github.com/first20hours/google-10000-english
#
###############################################################################

import itertools
import string

def enc_dec(iOrig, iKey):
    oDest = []
    for i, asc in enumerate(iOrig):
        key_i = iKey[i%len(iKey)]
        oDest.append(asc^ord(key_i))
    return oDest

# Test to remove##############################################################
#char_decr = 'Hello, this is a test'
#asc_decr = [ord(x) for x in char_decr]
#key='zzz' #97 98 99
#asc_encr = enc_dec(asc_decr, key)
##############################################################################

def euler059():
    with open("p059_dictionary.txt") as word_file:
        eng_set = set(word.strip().lower() for word in word_file)


    with open("p059_cipher.txt") as encripted_file:
        for asc in encripted_file:
            asc_encr=asc.split(sep=",")
    asc_encr = [int(x) for x  in asc_encr]

    lower = string.ascii_lowercase

    ## genera_keys y las prueba
    gen_keys = itertools.product(lower, repeat=3)
    for key in gen_keys:
        key = "".join(key) # aaa aab aac aba...
        decr = enc_dec(asc_encr, key) # 72 111 108...
        plain = "".join([chr(x) for x in decr])
        plainStripped = plain.strip()

        words = plainStripped.split()
        founds = 0
        for word in words:
            if word.lower() in eng_set:
                    founds +=1
        if founds >=50: # asumo mas de 50 palabras correctas...
            print("[{}] (key:[{}])".format(plain, key))
            sumAscii = 0
            for char in plain:
                sumAscii += ord(char)
            return sumAscii

if __name__ == "__main__":
    print(euler059())
    # 107359
