'''
Vowel Repeater
Given a string, return a new version of the string where each vowel is duplicated one more time than the previous vowel you encountered. For instance, the first vowel in the sentence should remain unchanged. The second vowel should appear twice in a row. The third vowel should appear three times in a row, and so on.

The letters a, e, i, o, and u, in either uppercase or lowercase, are considered vowels.
The original vowel should keeps its case.
Repeated vowels should be lowercase.
All non-vowel characters should keep their original case.
'''


def repeat_vowels(s):
    vowels = 'aeiouAEIOU'
    arr = []
    x = 0
    for i in s:
        if i in vowels:
            # print(x)
            i = i + (i.lower() * x)
            # print(i)
            arr.append(i)
            x = x + 1
            # print(x)
        else:
            arr.append(i)
        # print(arr)
    s = ''.join(arr)
    return s


t = repeat_vowels("hello world")
print(t)
