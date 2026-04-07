'''
Pi Day
Happy pi (π) day!

Given an integer (n), where n is between 1 and 1000 (inclusive), return the nth decimal of π.

Make sure to return a number not a string.
π with its first five decimals is 3.14159. So given 5 for example, return 9, the fifth decimal.

You may have to find the first 1000 decimals of π somewhere.
'''

from sympy import *
def get_pi_decimal(n):
    X = N(pi,n+1)
    # result =X[:-1]
    # print(result)
    result = str(X)
    print(X)
    print(result)

    print(result[-1])

    n = result[-1]

    return n

t = get_pi_decimal(5)
print(t)