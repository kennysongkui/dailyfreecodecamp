'''
Permutation Count
Given a string, return the number of distinct permutations that can be formed from its characters.

A permutation is any reordering of the characters in the string.
Do not count duplicate permutations.
If the string contains repeated characters, repeated arrangements should only be counted once.
The string will contain only letters (A-Z, a-z).
For example, given "abb", return 3 because there's three unique ways to arrange the letters: "abb", "bab", and "bba".
'''
from itertools import permutations

import math
from collections import Counter

def count_permutations(s):
    '''
    对于有重复字符的字符串，排列数为 n!/(n1! * n2! * ... * nk!)，其中n是字符串长度，n1, n2, ..., nk是每个字符出现的次数。
    :param s:
    :return:
    '''
    n = len(s)

    char_count = Counter(s)

    numerator = math.factorial(n)
    denominator = 1
    for count in char_count.values():
        denominator *= math.factorial(count)

    count = numerator // denominator
    print(count)
    s = count
    return s

# def count_permutations(s):
#
#     words = [''.join(p) for p in permutations(s)]
#     unique_arr = list(set(words))
#     print(words)
#     print(unique_arr)
#     s = len(unique_arr)
#     return s


# t = count_permutations("abb")
# print(t)

t1 = count_permutations("freecodecamp")
print(t1)