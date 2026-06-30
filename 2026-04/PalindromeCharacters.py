'''
Palindrome Characters
Given a string, determine if it's a palindrome and return the middle character (if it's odd length) or middle two characters (if it's even).

A palindrome is a string that is the same forward and backward.
If it's not a palindrome, return "none".
'''


def palindrome_locator(s):
    print(s[::-1])
    if s == s[::-1]:
        n = len(s)
        if n % 2 == 1:
            flag = s[n // 2]
        else:
            flag = s[n // 2 - 1:n // 2 + 1]
    else:
        flag = "none"

    print(flag)
    s = flag
    return s


t = palindrome_locator("racecar")
print(t)
