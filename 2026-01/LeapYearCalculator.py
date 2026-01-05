'''
Leap Year Calculator
Given an integer year, determine whether it is a leap year.

A year is a leap year if it satisfies the following rules:

The year is evenly divisible by 4, and
The year is not evenly divisible by 100, unless
The year is evenly divisible by 400.
'''

def is_leap_year(year):
    flag = False

    if (year % 4 == 0 and year % 100 !=0) or (year %400 == 0):
        flag = True
    print(flag)
    year = flag

    return year


t = is_leap_year(2024)
print(t)