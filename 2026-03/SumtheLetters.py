'''
Sum the Letters
Given a string, return the sum of its letters.

Letters are A-Z in uppercase or lowercase
Letter values are: "A" = 1, "B" = 2, ..., "Z" = 26
Uppercase and lowercase letters have the same value.
Ignore all non-letter characters.
'''


def sum_letters(s):

    total = 0
    for i in s:
        if i.isalpha():
            total += ord(i.upper()) - ord('A') + 1
    print(total)
    s = total
    return s


t = sum_letters("Hello")
