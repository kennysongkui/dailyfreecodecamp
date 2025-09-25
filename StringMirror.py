'''
String Mirror
Given two strings, determine if the second string is a mirror of the first.

A string is considered a mirror if it contains the same letters in reverse order.
Treat uppercase and lowercase letters as distinct.
Ignore all non-alphabetical characters.
'''
import re


def is_mirror(str1, str2):
    new_str1 = []
    new_str2 = []
    for i in range(len(str1)):
        if re.match(r'[a-zA-Z]', str1[i]):
            new_str1.append(str1[i])

    for i in range(len(str2)):
        if re.match(r'[a-zA-Z]', str2[i]):
            new_str2.append(str2[i])

    new_str2.reverse()
    # print(new_str2)
    if new_str1 == new_str2:
        str1 = True
    else:
        str1 = False

    return str1

t = is_mirror("helloworld", "helloworld")
print(t)
t1 = is_mirror("Hello World", "dlroW olleH")
print(t1)