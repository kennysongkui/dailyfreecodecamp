'''
Kaprekar's Routine
Given a 4-digit number, return the number of times you need to apply Kaprekar's routine until reaching 6174.

Kaprekar's routine works as follows:

Arrange the digits in descending order to form the largest number
Arrange the digits in ascending order to form the smallest number (pad with leading zeros if necessary)
Subtract the smaller from the larger
Repeat with the new number
'''


def kaprekar(n):
    count = 0
    while n != 6174:
        s = f"{n:04d}"
        asc = int(''.join(sorted(s)))
        desc = int(''.join(sorted(s, reverse=True)))
        n = desc - asc
        print(n)
        count += 1

        if n == 0:
            return -1
    n = count
    return n


t = kaprekar(1234)
print(t)
