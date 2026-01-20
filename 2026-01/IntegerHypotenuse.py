'''
Integer Hypotenuse
Given two positive integers representing the lengths for the two legs (the two short sides) of a right triangle, determine whether the hypotenuse is an integer.

The length of the hypotenuse is calculated by adding the squares of the two leg lengths together and then taking the square root of that total (a2 + b2 = c2).
'''

import math

def is_integer_hypotenuse(a, b):

    total = math.floor(math.pow(a, 2) + math.pow(b, 2))

    sqrt = pow(total, 0.5)
    print(total, sqrt)

    result = False

    if sqrt % 1 == 0:
        result = True


    a = result

    return a

t = is_integer_hypotenuse(3, 4)
print(t)

t1 = is_integer_hypotenuse(2, 3)
print(t1)