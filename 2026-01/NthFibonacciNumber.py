'''
Nth Fibonacci Number
Given an integer n, return the nth number in the fibonacci sequence.

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. The first 10 numbers in the sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.
'''

def nth_fibonacci(n):

    # def fibonacci(x):
    #     if x <= 1:
    #         return x
    #     else:
    #         return fibonacci(x -1) + fibonacci(x -2)
    #
    # result = fibonacci(n-1)
    # print(result)
    # n = result
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    prev, curr = 0, 1
    for i in range(2, n):
        prev, curr = curr, prev + curr

    result = curr
    print(result)
    n = result
    return n


t = nth_fibonacci(75)
print(t)