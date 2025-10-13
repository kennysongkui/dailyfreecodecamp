'''
Battle of Words
Given two sentences representing your team and an opposing team, where each word from your team battles the corresponding word from the opposing team, determine which team wins using the following rules:

The given sentences will always contain the same number of words.
Words are separated by a single space and will only contain letters.
The value of each word is the sum of its letters.
Letters a to z correspond to the values 1 through 26. For example, a is 1, and z is 26.
A capital letter doubles the value of the letter. For example, A is 2, and Z is 52.
Words battle in order: the first word of your team battles the first word of the opposing team, and so on.
A word wins if its value is greater than the opposing word's value.
The team with more winning words is the winner.
Return "We win" if your team is the winner, "We lose" if your team loses, and "Draw" if both teams have the same number of wins.
'''


def battle(our_team, opponent):
    letter_dict = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26,
        "A": 2,
        "B": 4,
        "C": 6,
        "D": 8,
        "E": 10,
        "F": 12,
        "G": 14,
        "H": 16,
        "I": 18,
        "J": 20,
        "K": 22,
        "L": 24,
        "M": 26,
        "N": 28,
        "O": 30,
        "P": 32,
        "Q": 34,
        "R": 36,
        "S": 38,
        "T": 40,
        "U": 42,
        "V": 44,
        "W": 46,
        "X": 48,
        "Y": 50,
        "Z": 52,
    }

    new_our = our_team.split()
    new_opp = opponent.split()

    new_flag = 0
    opp_flag = 0

    for i in range(len(new_our)):
        new_total = 0
        opp_total = 0
        for x in list(new_our[i]):
            new_total += letter_dict[x]
            # print(new_total)
        for y in list(new_opp[i]):
            opp_total += letter_dict[y]
            # print(y)
            # print(opp_total)
        print(new_total)
        print(opp_total)
        if new_total > opp_total:
            new_flag += 1
        elif new_total < opp_total:
            opp_flag += 1
        else:
            continue

    if new_flag > opp_flag:
        our_team = "We win"
    elif new_flag < opp_flag:
        our_team = "We lose"
    else:
        our_team = "Draw"

    return our_team


t = battle("hello world", "hello word")
print(t)

t1 = battle("hello world", "world hello")
print(t1)