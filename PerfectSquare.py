'''
Perfect Square
Given an integer, determine if it is a perfect square.

A number is a perfect square if you can multiply an integer by itself to achieve the number. For example, 9 is a perfect square because you can multiply 3 by itself to get it.
'''
import math


def is_perfect_square(n):
    if n >= 0:
        x = math.sqrt(n)
        if (x % 1 == 0):
            n = True
        else:
            n = False
    else:
        n = False
    return n


t = is_perfect_square(9)
print(t)
t1 = is_perfect_square(-9)
print(t1)
