'''
Odd or Even?
Given a positive integer, return "Odd" if it's an odd number, and "Even" is it's even.
'''

def odd_or_even(n):

    result = None
    if n % 2 == 0:
        result = 'Even'
    else:
        result = "Odd"

    n = result

    return n

t = odd_or_even(123456789)
print(t)