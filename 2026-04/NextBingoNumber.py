'''
Next Bingo Number
Given a bingo number, return the next bingo number sequentially.

A bingo number is a single letter followed by a number in its range according to this chart:

Letter	Number Range
"B"	1-15
"I"	16-30
"N"	31-45
"G"	46-60
"O"	61-75
For example, given "B10", return "B11", the next bingo number. If given the last bingo number, return "B1".
'''


def get_next_bingo_number(n):
    ranges = {
        "B": (1, 15),
        "I": (16, 30),
        "N": (31, 45),
        "G": (46, 60),
        "O": (61, 75)
    }
    text = n[0]
    number = int(n[1:])

    min_num, max_num = ranges[text]
    if number < max_num:
        next_num = number + 1
        next_text = text
    else:
        letters = ["B", "I","N", "G", "O"]
        idx = letters.index(text)
        if idx == len(letters) -1:
            next_text = letters[0]
            next_num = ranges[next_text][0]
        else:
            next_text = letters[idx +1]
            next_num = ranges[next_text][0]

    result = f"{next_text}{next_num}"
    print(result)

    # print(text, number)

    n = result
    return n


t = get_next_bingo_number("B10")
print(t)
