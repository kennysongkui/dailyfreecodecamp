'''
Counting Cards
A standard deck of playing cards has 13 unique cards in each suit. Given an integer representing the number of cards to pick from the deck, return the number of unique combinations of cards you can pick.

Order does not matter. Picking card A then card B is the same as picking card B then card A.
For example, given 52, return 1. There's only one combination of 52 cards to pick from a 52 card deck. And given 2, return 1326, There's 1326 card combinations you can end up with when picking 2 cards from the deck.
'''

import math
def combinations(cards):
    total_cards = 52
    result = 0
    if cards < 0 or cards > total_cards:
        result = 0
    if cards == 0:
        result = 1

    result = math.comb(total_cards, cards)
    print(result)
    cards = result
    return cards

t = combinations(45)
print(t)

t1 = combinations(23)
print(t1)