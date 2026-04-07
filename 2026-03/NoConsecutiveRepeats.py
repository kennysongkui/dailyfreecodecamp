'''
No Consecutive Repeats
Given a string, determine if it has no repeating characters.

A string has no repeats if it does not have the same character two or more times in a row.

'''


def has_no_repeats(s):

    for i in range(len(s) -1):
        if s[i] == s[i+1]:
            return False
    result = True

    s = result

    return s


# t = has_no_repeats("hi world")
# print(t)

t1 = has_no_repeats("The quick brown fox jumped over the lazy dog.")
print(t1)
