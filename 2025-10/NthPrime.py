'''
Nth Prime
A prime number is a positive integer greater than 1 that is divisible only by 1 and itself. The first five prime numbers are 2, 3, 5, 7, and 11.

Given a positive integer n, return the nth prime number. For example, given 5 return the 5th prime number: 11.


'''
import math

def nth_prime(n):
    if n <= 0:
        raise ValueError("n > 0")

    count = 0
    num = 1

    while count < n :
        num += 1
        if is_prime(num):
            count += 1
    n = num
    return n


def is_prime(num):
    if num <= 1:
        return False

    if num == 2:
        return True

    if num % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(num)) +1 , 2):
        if num % i  == 0:
            return False
    return True


t = nth_prime(10)
print(t)

t1 = nth_prime(1000)
print(t1)
