'''
Largest Number
Given a string of numbers separated by various punctuation, return the largest number.

The given string will only contain numbers and separators.
Separators can be commas (","), exclamation points ("!"), question marks ("?"), colons (":"), or semi-colons (";").
'''

import re
def largest_number(s):
    pattern = r'\d+'
    test = re.split(r'[!,?;:]+',s)
    print(type(test))

    # for i in test:
    #     print(i)
    numbers = [float(i) for i in test if i ]
    result = max(numbers)
    print(result)

    s = result
    return s

# t = largest_number("1,2")
# print(t)

t1 = largest_number("-402,-1032!-569:-947;-633?-800!-1012;-402,-723?-8102!-3011")
print(t1)