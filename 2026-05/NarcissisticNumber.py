'''
Narcissistic Number
Given a positive integer, determine whether it is a narcissistic number.

A number is narcissistic if the sum of each of its digits raised to the power of the total number of digits equals the number itself.
For example, 153 has 3 digits, and 13 + 53 + 33 = 153, so it is narcissistic.
'''

def is_narcissistic(n):
    digits = []
    x = n
    if n == 0:
        digits = 0
    else:
        while n > 0:
            digits.append(n % 10)
            n = n // 10
    print(digits)
    digits_len = len(digits)
    print(digits_len)
    result = 0
    for i in digits:
        result += pow(i, digits_len)
    print(result)
    print(n)
    if result == x :
        return True
    else:
        return False

    return n

t = is_narcissistic(153)
print(t)