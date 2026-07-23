'''
Parentheses Combinations
Given an integer, n, return the number of valid combinations of n pairs of parentheses.

A valid combination is a string where every opening parentheses has a corresponding closing parentheses, and no closing parentheses appears before its matching opening parentheses.
For example, given 2, there are 2 valid combinations:

(())
()()
'''

import math


def get_combinations(n):
    result = math.comb(2 * n, n) // (n + 1)
    print(result)
    n = result
    return n


t = get_combinations(2)
print(t)
