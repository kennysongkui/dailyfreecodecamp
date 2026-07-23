'''
Bingo Range
Given a bingo letter, return the number range associated with that letter.

Letter	Number Range
"B"	1-15
"I"	16-30
"N"	31-45
"G"	46-60
"O"	61-75
Return an array with all numbers in the range from smallest to largest.
'''


def get_bingo_range(letter):
    ranges = {
        'B': list(range(1, 16)),
        'I': list(range(16, 31)),
        'N': list(range(31, 46)),
        'G': list(range(46, 61)),
        'O': list(range(61, 76))
    }

    result = ranges[letter.upper()]
    print(result)
    letter = result
    return letter


# t = get_bingo_range("B")
# print(t)

t1 = get_bingo_range("I")
print(t1)