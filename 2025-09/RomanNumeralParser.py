'''
Roman Numeral Parser
Given a string representing a Roman numeral, return its integer value.

Roman numerals consist of the following symbols and values:

Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000
Numerals are read left to right. If a smaller numeral appears before a larger one, the value is subtracted. Otherwise, values are added.
'''


def parse_roman_numeral(numeral):
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    arr = reversed(list(numeral))
    # print(arr)
    total = 0
    prev= 0
    for i in arr:
        value = roman_dict[i]
        if value < prev:
            total = total - value
        else:
            total += value
        prev = value
    numeral = total
    return numeral


t = parse_roman_numeral("MMXXV")
print(t)

t1 = parse_roman_numeral("IV")
print(t1)
