'''
Parsec Converter
In a distant galaxy, parsecs are used to measure both time and distance. Given an integer number of parsecs, return its equivalent in time or distance.

If the given integer is odd, it represents time. If it's even, it represents distance.
Use these conversion rates:

Parsecs	Time/Distance
1	2 hours
2	6 light years
Return the converted value as an integer.
'''


def convert_parsecs(parsecs):
    result = 0

    if parsecs % 2 == 0:
        result = (parsecs / 2) * 6
    else:
        result = parsecs * 2
    print(result)
    parsecs = result
    return parsecs


t = convert_parsecs(1)
print(t)
