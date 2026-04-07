'''
Playing Card Values
Given an array of playing cards, return a new array with the numeric value of each card.

Card Values:

An Ace ("A") has a value of 1.
Numbered cards ("2" - "10") have their face value: 2 - 10, respectively.
Face cards: Jack ("J"), Queen ("Q"), and King ("K") are each worth 10.
Suits:

Each card has a suit: Spades ("S"), Clubs ("C"), Diamonds ("D"), or Hearts ("H").
Card Format:

Each card is represented as a string: "valueSuit". For Example: "AS" is the Ace of Spades, "10H" is the Ten of Hearts, and "QC" is the Queen of Clubs.

'''


def card_values(cards):
    face_cards = ["J", "Q", "K"]
    result = []
    for i in cards:

        x = i[:-1]

        if x == "A":
            result.append(1)
        elif x in face_cards:
            result.append(10)
        else:
            result.append(int(x))

    print(result)
    cards = result[:]
    return cards


# t = card_values(["3H", "4D", "5S"])
# print(t)

t1 = card_values(["AS", "10S", "10H", "6D", "7D"])
print(t1)
