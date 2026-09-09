'''
Letter Distance
Given two strings of equal length, return the sum of the shortest distances between each pair of characters.

The input will only contain lowercase letters
The alphabet is treated as a circle, so the distance between a and z is 1.
'''


def letter_distance(str1, str2):
    total = 0
    for a, b in zip(str1, str2):
        diff = abs(ord(a) - ord(b))
        total += min(diff, 26 - diff)
    print(total)
    str1 = total
    return str1


t = letter_distance("abc", "bcd")
print(t)
