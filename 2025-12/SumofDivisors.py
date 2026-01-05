'''
Sum of Divisors
Given a positive integer, return the sum of all its divisors.

A divisor is any integer that divides the number evenly (the remainder is 0).
Only count each divisor once.
For example, given 6, return 12 because the divisors of 6 are 1, 2, 3, and 6, and the sum of those is 12.
'''


def sum_divisors(n):
    result = n
    for i in range(1, n):
        if n % i == 0:
            result += i
            print(i)
    print(result)
    n = result
    return n


# t = sum_divisors(6)
# print(t)

t1 = sum_divisors(9348)
print(t1)
