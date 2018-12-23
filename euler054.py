#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    EULER 054
        In the card game poker, a hand consists of five cards and are ranked,
        from lowest to highest, in the following way:

            High Card: Highest value card.
            One Pair: Two cards of the same value.
            Two Pairs: Two different pairs.
            Three of a Kind: Three cards of the same value.
            Straight: All cards are consecutive values.
            Flush: All cards of the same suit.
            Full House: Three of a kind and a pair.
            Four of a Kind: Four cards of the same value.
            Straight Flush: All cards are consecutive values of same suit.
            Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

        The cards are valued in the order:
        2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

        If two players have the same ranked hands then the rank made
        up of the highest value wins; for example, a pair of eights beats
        a pair of fives (see example 1 below). But if two ranks tie,
        for example, both players have a pair of queens, then highest
        cards in each hand are compared (see example 4 below); if the
        highest cards tie then the next highest cards are compared, and so on.

        Consider the following five hands dealt to two players:
        Hand	 	Player 1	  	     Player 2	      Winner
        1	 	5H 5C 6S 7S KD       2C 3S 8S 8D TD      Player 2
                Pair of Fives        Pair of Eights

        2	 	5D 8C 9S JS AC       2C 5C 7D 8S QH      Player 1
               Highest card Ace     Highest card Queen

        3	 	2D 9C AS AH AC       3D 6D 7D TD QD      Player 2
                  Three Aces       Flush with Diamonds

        4	 	4D 6S 9H QH QC 	     3D 6D 7H QD QS   	 Player 1
                 Pair of Queens       Pair of Queens
                Highest card Nine   Highest card Seven

        5	 	2H 2D 4C 4D 4S       3C 3D 3S 9S 9D      Player 1
                  Full House         Full House
               With Three Fours     with Three Threes

        The file, poker.txt, contains one-thousand random hands dealt
        to two players. Each line of the file contains ten cards
        (separated by a single space): the first five are Player 1's cards
        and the last five are Player 2's cards. You can assume that all
        hands are valid (no invalid characters or repeated cards), each
        player's hand is in no specific order,
        and in each hand there is a clear winner.

        How many hands does Player 1 win?
"""
# =============================================================================
# (upper left label is the current label)
#
# SOLUTION: 376
#
# STATUS: [ok]
# VERIFIED: [no/ok]
# EXECUTION TIME: [ok]
# =============================================================================

DICO_CARD_VALUES = {'2':2,
                    '3':3,
                    '4':4,
                    '5':5,
                    '6':6,
                    '7':7,
                    '8':8,
                    '9':9,
                    'T':10,
                    'J':11,
                    'Q':12,
                    'K':13,
                    'A':14}

C_ROYAL_FLUSH = 10
C_STRAIGHT_FLUSH = 9
C_FLUSH = 6
C_STRAIGHT = 5
C_FOUR_KIND = 8
C_THREE_KIND = 4
C_FULL_HOUSE = 7
C_ONE_PAIR = 2
C_TWO_PAIR = 3
C_HIGHEST = 1


def evaluate_hands(hand1, hand2):
    for value1, value2 in zip(hand1, hand2):
        if value1 > value2:
            return 1
        elif value2 > value1:
            return 2


def identify_hand(hand):
    dico_values = {}
    dico_suits = {}

    hand = hand.split()

    # Ordenar las cartas de mayor a menor
    #
    hand = sorted(hand, key=lambda x: DICO_CARD_VALUES.get(x[0]),reverse=True)
#    print("")
#    print("Hand sorted: {}".format(hand))

    # Parser solo una vez..
    #
    first_value = DICO_CARD_VALUES[hand[0][0]]
    consecutive = 1
    for card in hand:
        value = DICO_CARD_VALUES[card[0]]
        suit = card[1]
        dico_values[value] = dico_values.get(value, 0) + 1
        dico_suits[suit] = dico_suits.get(suit, 0) + 1

        if value is first_value - 1:
            first_value = value
            consecutive += 1

    if 5 in dico_suits.values():
        if consecutive is 5:
            if hand[0][0] is "A":
#                print("Royal Flush!")
                return [C_ROYAL_FLUSH]
            else:
#                print("Straight Flush de {}".format(DICO_CARD_VALUES[hand[0][0]]))
                return [C_STRAIGHT_FLUSH, DICO_CARD_VALUES[hand[0][0]]]
        else:
#            print("Flush de {}".format(DICO_CARD_VALUES[hand[0][0]]))
            return [C_FLUSH, DICO_CARD_VALUES[hand[0][0]]]
    elif consecutive is 5:
#        print("Straight de {}".format(DICO_CARD_VALUES[hand[0][0]]))
        return [C_STRAIGHT, DICO_CARD_VALUES[hand[0][0]]]
#########################################################
    pair_found = False

    full_house = False
    three = False
    two_pair = False
    one_pair = False

    full_value = 0
    three_value = 0
    two_value = 0
    pair_value = 0

    remaining = []
    for value,frequency in dico_values.items():
        if frequency is 4:
#            print("Four of a kind de {}".format(value))
            return [C_FOUR_KIND, value]

        if frequency is 3:
            if 2 in dico_values.values():
                full_house = True
                full_value = value
            else:
                three = True
                three_value = value
        if frequency is 2:
            if pair_found == True:
                two_pair = True
                two_value = value
            else:
                one_pair = True
                pair_found = True
                pair_value = value
        else:
            remaining.append(value)

    if full_house:
#        print("Full House de {}".format(full_value))
        return [C_FULL_HOUSE, full_value]
    elif three:
#        print("Three of a Kind de {}".format(three_value))
        return [C_THREE_KIND, three_value]
    elif two_pair:
#        print("Two pairs {} ({})".format(two_value, remaining))  # PUEDE EMPATAR
        return [C_TWO_PAIR] + [two_value] + remaining
    elif one_pair:
#        print("One Pair de {} ({})".format(pair_value, remaining)) # PUEDE EMPATAR
#        print([C_ONE_PAIR].extend(remaining))
        return [C_ONE_PAIR]+ [pair_value] + remaining
    else:
#        print("Highest de {} ({})".format(DICO_CARD_VALUES[hand[0][0]], remaining)) # PUEDE EMPATAR
        return [C_HIGHEST]+remaining



def euler054():
    # 1 leer el fichero linea a linea y separar jugada 1 de jugada 2
    player_one_wins = 0
    with open("p054_poker.txt") as fhandle:
        for line in fhandle:
            line = line.strip()
            player1 = line[:14] # el formato es fijo
            player2 = line[15:] # el formato es fijo

#            print("#################################################")
#            print("#")

            hand_player_1 = identify_hand(player1)
            hand_player_2 = identify_hand(player2)

#            print("Player1: {}    Player2: {}".format(hand_player_1,hand_player_2))
            if evaluate_hands(hand_player_1, hand_player_2) is 1:
                player_one_wins +=1
#                print("Player one wins")
            elif evaluate_hands(hand_player_1, hand_player_2) is 2:
                pass
#                 print("Player two wins")
            else:
                print("EMPATE!!!")
    return player_one_wins

if __name__ == "__main__":
    print(euler054())
    # 376
