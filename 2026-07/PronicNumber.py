'''
Pronic Number
Given a number, determine whether it is a pronic number.

A pronic number is the product of two consecutive integers. For example, 6 is pronic because 2 * 3 = 6.

'''


def is_pronic(n):
    if n < 0:
        return False

    i = 0
    while i * (i + 1) <= n:
        if i * (i + 1) == n:
            return True
        i += 1
        print(i)
    result = False
    n = result
    return n


t = is_pronic(132000)
print(t)
