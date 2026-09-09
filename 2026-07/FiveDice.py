'''
Five Dice
Given an array of five dice with values 1-6, return the best possible hand.

Here are the hands ranked lowest to highest:

Hand	Description
"no pair"	No pair or better
"pair"	Two dice with the same value
"two pair"	Two different pairs
"three of a kind"	Three dice with the same value
"small straight"	Four consecutive values
"large straight"	Five consecutive values
"full house"	Three of a kind and a pair
"four of a kind"	Four dice with the same value
"five of a kind"	All five dice with the same value

'''


def five_dice(dice):
    counts = [0] * 7
    print(counts)

    for d in dice:
        counts[d] += 1
    print(counts)

    sorted_counts = sorted(counts[1:], reverse=True)
    if sorted_counts[0] == 5:
        return "five of a kind"

    if sorted_counts[0] == 4:
        return "four of a kind"

    if sorted_counts[0] == 3 and sorted_counts[1] == 2:
        return "full house"

    unique = sorted(set(dice))

    if len(unique) == 5:
        if unique == [1, 2, 3, 4, 5] or unique == [2, 3, 4, 5, 6]:
            return "large straight"
    if len(unique) >= 4:
        for i in range(len(unique) - 3):
            if unique[i + 3] - unique[i] == 3:
                return "small straight"

    if sorted_counts[0] == 3:
        return "three of a kind"

    if sorted_counts[0] == 2 and sorted_counts[1] == 2:
        return "two pair"

    if sorted_counts[0] == 2:
        return "pair"

    return "no pair"


t = five_dice([1, 1, 1, 1, 1])
print(t)
