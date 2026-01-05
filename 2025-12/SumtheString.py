'''
Sum the String
Given a string containing digits and other characters, return the sum of all numbers in the string.

Treat consecutive digits as a single number. For example, "13" counts as 13, not 1 + 3.
Ignore any non-digit characters.
'''

import re


def string_sum(s):
    new_arr = re.findall(r'\d+', s)
    print(new_arr)
    result = 0
    for i in new_arr:
        result += int(i)

    print(result)
    s = result
    return s


t = string_sum("3apples2bananas")
print(t)

t1 = string_sum("10cats5dogs2birds")
print(t1)

t2 = string_sum("125344")
print(t2)
