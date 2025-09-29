'''
Acronym Builder
Given a string containing one or more words, return an acronym of the words using the following constraints:

The acronym should consist of the first letter of each word capitalized, unless otherwise noted.
The acronym should ignore the first letter of these words unless they are the first word of the given string: a, for, an, and, by, and of.
The acronym letters should be returned in the order they are given.
The acronym should not contain any spaces.
'''


def build_acronym(s):
    other_arr = ['a', 'for', 'an', 'and', 'by', 'of']
    arr = s.split()
    new_arr = []
    for i in range(len(arr)):
        if i == 0:
            new_arr.append(list(arr[i])[0].upper())
            continue
        if arr[i].lower() not in other_arr:
            new_arr.append(list(arr[i])[0].upper())
    # print(arr)
    # print(new_arr)
    s = ''.join(new_arr)
    return s


t = build_acronym("Search Engine Optimization")
print(t)
