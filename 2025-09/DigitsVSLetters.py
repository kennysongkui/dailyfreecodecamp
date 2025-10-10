'''
Digits vs Letters
Given a string, return "digits" if the string has more digits than letters, "letters" if it has more letters than digits, and "tie" if it has the same amount of digits and letters.

Digits consist of 0-9.
Letters consist of a-z in upper or lower case.
Ignore any other characters.
'''
import re
def digits_or_letters(s):
    sum_dig = 0
    sum_str = 0
    for i in s:
        if  re.match(r'[0-9]', i) :
            sum_dig += 1
        elif re.match(r'[a-zA-Z]', i):
            sum_str += 1
        else:
            pass
    if sum_dig > sum_str :
        s = "digits"
    elif sum_dig < sum_str :
        s = "letters"
    else:
        s = "tie"
        print
    return s

t = digits_or_letters("abc123")
print(t)
t1 = digits_or_letters("a1b2c3d")
print(t1)

t2 = digits_or_letters("H3110 W0R1D")
print(t2)