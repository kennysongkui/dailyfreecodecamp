'''
Best Hand
Given an array of five strings representing playing cards, return the name of the best hand.

Each card is represented as a two-character string: the rank followed by the suit, "2h" for example.
Ranks, from low to high, are: "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", and "A".
Suits are: "h", "d", "c", and "s".
Aces ("A") can be used as high or low in a straight.
The hands, in order from worst to best, are:

Name	Description
"High Card"	No pair or better
"Pair"	Two of one rank
"Two Pair"	Two of one rank and two of another
"Three of a Kind"	Three of one rank
"Straight"	Five ranks in a row
"Flush"	Five of the same suit
"Full House"	Three of one rank, and two of another
"Four of a Kind"	Four of one rank
"Straight Flush"	Five ranks in a row of the same suit
"Royal Flush"	"A", "K", "Q", "J", "T" of the same suit
Return the name of the best hand.
'''

from collections import Counter


def get_best_hand(cards):
    ranks = [card[0] for card in cards]
    suits = [card[1] for card in cards]
    print(ranks, suits)

    rank_value = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
        '7': 7, '8': 8, '9': 9, 'T': 10,
        'J': 11, 'Q': 12, 'K': 13, 'A': 14
    }
    values = [rank_value[r] for r in ranks]

    suit_counts = Counter(suits)

    is_flush = any(c == 5 for c in suit_counts.values())

    def is_straight(vals):
        vals = sorted(vals)

        if all(vals[i + 1] - vals[i] == 1 for i in range(4)):
            return True

        if 14 in vals:
            ace_low = [1 if v == 14 else v for v in vals]
            ace_low.sort()
            if all(ace_low[i + 1] - ace_low[i] == 1 for i in range(4)):
                return True
        return False

    straight = is_straight(values)

    rank_counts = Counter(ranks)
    counts = sorted(rank_counts.values(), reverse=True)

    if is_flush and straight:
        if sorted(values) == [10, 11, 12, 13, 14]:
            return "Royal Flush"
        return "Straight Flush"

    if 4 in counts:
        return "Four of a Kind"

    if counts == [3, 2]:
        return "Full House"

    if is_flush:
        return "Flush"

    if straight:
        return "Straight"

    if 3 in counts:
        return "Three of a Kind"

    if counts == [2, 2, 1]:
        return "Two Pair"

    if 2 in counts:
        return "Pair"

    cards = "High Card"

    return cards


t = get_best_hand(["7s", "7h", "7d", "2c", "5h"])
print(t)
