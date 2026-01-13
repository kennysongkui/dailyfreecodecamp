'''
Circular Prime
Given an integer, determine if it is a circular prime.

A circular prime is an integer where all rotations of its digits are themselves prime.

For example, 197 is a circular prime because all rotations of its digits: 197, 971, and 719, are prime numbers.
'''


def is_circular_prime(n):
    rotations = []
    s = str(n)
    length = len(s)

    for i in range(length):
        rotation = int(s[i:] + s[:i])
        rotations.append(rotation)
    print(rotations)

    for ratation in rotations:
        if not is_prime(ratation):
            return False
    n = True

    return n

def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


t = is_circular_prime(197)
print(t)
