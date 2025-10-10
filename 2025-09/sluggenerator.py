'''
Given a string, return a URL-friendly version of the string using the following constraints:

All letters should be lowercase.
All characters that are not letters, numbers, or spaces should be removed.
All spaces should be replaced with the URL-encoded space code %20.
Consecutive spaces should be replaced with a single %20.
The returned string should not have leading or trailing %20.
'''

import re
def generate_slug(str):
    test = re.sub(r'^\s+|\s+$', '', str.lower())
    print(test)
    # test1 = re.sub(r'\s+', '%20', test)
    test2 = test.split()
    test3 =[]
    for i in test2:
        sub = re.sub(r'\W+','', i)
        test3.append(sub)
    str = '%20'.join(test3)
    # # print(test1)
    # test2 = re.sub(r'\W+','', test1)
    # # test2 = re.sub(r'\s+','%20', test1)
    # print(test2)
    #
    #
    # str = test2
    return str

t = generate_slug("  ?H^3-1*1]0! W[0%R#1]D  ")
print(t)

t1 = generate_slug("helloWorld")
print(t1)