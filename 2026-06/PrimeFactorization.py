'''
Prime Factorization
Given an integer greater than 1, return its prime factorization as an array of numbers in ascending order.

A prime factorization is the set of prime numbers that multiply together to produce the given integer. Each number has exactly one set. For example, the prime factorization of 20 is [2, 2, 5] because 2 * 2 * 5 = 20.

If the given integer is itself prime, return it in a single-element array.
'''


def prime_factorization(n):
    factors = []
    d = 2
    while n % d == 0:
        factors.append(d)
        print(n)
        n //= d

    d = 3
    print(n)
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            print(n)
            n //= d
        d += 2

    print(n)
    if n > 1:
        factors.append(n)

    print(factors)

    n = factors
    return n


# t = prime_factorization(20)
# print(t)

t1 = prime_factorization(360)
print(t1)