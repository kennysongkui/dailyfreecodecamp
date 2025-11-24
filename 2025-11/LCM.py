'''
LCM
Given two integers, return the least common multiple (LCM) of the two numbers.

The LCM of two numbers is the smallest positive integer that is a multiple of both numbers. For example, given 4 and 6, return 12 because:

Multiples of 4 are 4, 8, 12 and so on.
Multplies of 6 are 6, 12, 18 and so on.
12 is the smallest number that is a multiple of both.
'''

def lcm(a, b):
    multiple = a
    while multiple % b != 0:
        multiple += a
    print(multiple)
    a = multiple
    return a

t = lcm(10, 100)
print(t)

t1 = lcm(9, 6)
print(t)
